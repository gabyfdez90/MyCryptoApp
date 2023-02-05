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


@app.route("/")
def index():
    return render_template('index.html')

@app.route(f"/api/{VERSION}/all")
def show_transactions():
    try:
        transaction_history = select_all()
        return jsonify (
            {"data": transaction_history,
            "status": "OK"}
        ), HTTPStatus.OK
    except sqlite3.Error as e:
        return jsonify(
            {
            "data": str(e),
            "status": "Error"
            }
        ), HTTPStatus.BAD_REQUEST
    
@app.route(f"/api/{VERSION}/tasa/<string:currency_from>/<string:currency_to>")
def get_rate_transactions(currency_from, currency_to):
    try:
        rate= apply_exchange(currency_from, currency_to)
        return jsonify (
            {"data": rate,
            "status": "OK"}
        ), HTTPStatus.OK
    except sqlite3.Error as e:
        return jsonify(
            {
            "data": str(e),
            "status": "Error"
            }
        ), HTTPStatus.BAD_REQUEST
