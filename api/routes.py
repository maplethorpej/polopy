import requests as r
import time

from api import app, cache, poloniex_url
from api.lib import TimeRange, range_periods
from flask import jsonify, request
from requests import RequestException


@app.route('/public', methods=['GET'])
def index():
    command = request.args.get('command')

    if command == 'returnTicker':
        @cache.cached(timeout=5, key_prefix=command)
        def get_ticker():
            ticker = r.get(poloniex_url + '?command=' + command)
            data = {'poloniex': ticker.json()}
            return jsonify(data)

        return get_ticker()

    if command == 'returnChartData':
        currencies_param = request.args.get('currencyPair')
        range_param = request.args.get('range')

        try:
            timeout = range_periods[range_param]['expires']
        except KeyError:
            return jsonify({'error': 'Invalid range specified.'
                                     'Accepted: LAST_HOUR, LAST_DAY, LAST_WEEK, LAST_MONTH, LAST_YEAR, ALL_TIME'})

        @cache.memoize(timeout=timeout)
        def get_chart_data(currencies, time_range):
            time_period = TimeRange(time_range=time_range)
            url = poloniex_url + '?command=' + command + '&' + time_period.get_query_str + '&currencyPair=' + currencies

            try:
                chart_data = r.get(url, timeout=30)
            except RequestException as e:
                return jsonify({'error': str(e)})

            data = {'poloniex': chart_data.json()}
            return jsonify(data)

        return get_chart_data(currencies_param, range_param)

    return jsonify({'error': 'Invalid or missing command parameter.'})


@app.route('/', defaults={'path': ''}, methods=['GET'])
@app.route('/<path:path>')
def catch_all(path):
    return jsonify({'error': 'Unknown endpoint.'})
