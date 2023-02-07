from flask import Flask
from flask_cors import CORS
from flask import render_template, jsonify, request
from app_crypto.models import *
import sqlite3
from http import HTTPStatus
from config import *
from app_crypto import app
from datetime import datetime, date

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
            {"status":"OK",
            "rate": rate,
            "currencies": [currency_from, currency_to]}
        ), HTTPStatus.OK
    except sqlite3.Error as e:
        return jsonify(
            {
            "data": str(e),
            "status": "Error"
            }
        ), HTTPStatus.BAD_REQUEST

@app.route(f"/api/{VERSION}/new",methods=["POST"])
def new():
    registrer = request.json
    time = datetime.now()
    money_available= calculate_currency_amount(registrer['quantity_from'])
    if registrer['currency_from'] != "EUR" and money_available < registrer['quantity_from']:
        return jsonify(
            {
                "status": "fail",
                "message": "Saldo insuficiente"
            }),HTTPStatus.BAD_REQUEST
    try:
        insert([date.today(),
                time.strftime("%H:%M:%S"),
                registrer['currency_from'],
                registrer['quantity_from'],
                registrer['currency_to'],
                registrer['quantity_to']])
        return jsonify(
            {
                "status": "success",
                "transaction": f"{registrer['currency_from']} to {registrer['currency_to']}"
            }
        ),HTTPStatus.CREATED 
    except sqlite3.Error as e:
        return jsonify(
            {
                "data": str(e),
                "status": "Error"
            }
        ),HTTPStatus.BAD_REQUEST