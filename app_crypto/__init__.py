from flask import Flask
from flask_cors import CORS
from flask import render_template, jsonify, request
from app_crypto.models import *
import sqlite3
from http import HTTPStatus
from config import *


app = Flask(__name__,instance_relative_config=True)
app.config.from_object('config')
CORS(app)

from app_crypto.routes import *
