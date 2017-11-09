from flask import Flask
from flask_cors import CORS
from flask_caching import Cache

app = Flask(__name__)
CORS(app)

redis_cache = {
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_HOST': '127.0.0.1',
    'CACHE_REDIS_PORT': '6379'
}

cache = Cache(config=redis_cache)
cache.init_app(app)

#with app.app_context():
#    cache.clear()

poloniex_url = 'https://poloniex.com/public'

app.config['SECRET_KEY'] = b'\xc3n\xf8F7)\xf5\x97a2m\x09yx\xa5\x02\x8e~]H\x9e\x1c\xb9\xe8'

import api.routes
