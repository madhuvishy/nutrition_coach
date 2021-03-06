from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import os

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
CORS(app)


from api import *
from models import *

if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), port=8081)