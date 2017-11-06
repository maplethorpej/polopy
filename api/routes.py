from api import app
from flask import Flask


@app.route('/', methods=['GET'])
def index():
    return 'index'
