import requests as r
import time

from api import app, cache
from flask import Flask, jsonify


@app.route('/', methods=['GET'])
@cache.cached(timeout=5)
def index():
    # poloniex_url = 'https://poloniex.com/public'
    # test_data = r.get(
    #     poloniex_url + '?command=returnChartData&currencyPair=BTC_XMR&start=1405699200&end=1406700000&period=14400')
    # print(test_data.json())
    # return jsonify(test_data.json())
    return time.ctime()
