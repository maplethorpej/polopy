from api import app
from flask import Flask
from poloniex import Poloniex
polo = Poloniex()


@app.route('/', methods=['GET'])
def index():
    return 'index'
