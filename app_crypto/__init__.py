from flask import Flask
from flask_cors import CORS
from app_crypto.models import *
from config import *


app = Flask(__name__,instance_relative_config=True)
app.config.from_object('config')
CORS(app, resources={r"/*": {"origins": "*"}})

from app_crypto.routes import *
