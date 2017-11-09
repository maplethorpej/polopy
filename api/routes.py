import requests as r
import time

from api import app, cache, poloniex_url
from flask import Flask, jsonify, request


@app.route('/public', methods=['GET'])
def index():
    command = request.args.get('command')

    @cache.cached(timeout=5, key_prefix=command)
    def get_ticker():
        ticker = r.get(poloniex_url + '?command=' + command)
        return jsonify(ticker.json())

    if command == 'returnTicker':
        return get_ticker()

    #
    # test_data = r.get(
    #     poloniex_url + '?command=returnChartData&currencyPair=BTC_XMR&start=1405699200&end=1406700000&period=14400')
    # print(test_data.json())
    # return jsonify(test_data.json())


    # keep the chartData stuff inside an object called poloniex
    return time.ctime()
