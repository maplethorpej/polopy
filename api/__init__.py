from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = b'\xc3n\xf8F7)\xf5\x97a2m\x09yx\xa5\x02\x8e~]H\x9e\x1c\xb9\xe8'

import api.routes
