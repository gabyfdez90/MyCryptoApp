from flask import Flask
from flask_cors import CORS
from flask import render_template, jsonify, request
from app_crypto.models import *
import sqlite3
from http import HTTPStatus
from config import *
from app_crypto import app
from datetime import datetime, date
from flask_cors import cross_origin

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
        rate= get_transaction_rate(currency_from, currency_to)
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
    money_available= calculate_currency_amount(registrer["currency_from"])
    if registrer['currency_from'] != "EUR" and float(registrer["quantity_from"]) > money_available:
         return jsonify(
             {
                 "status": "fail",
                "message": "Saldo insuficiente"
            }),HTTPStatus.ACCEPTED
    else:
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
                    "transaction": f"{registrer['currency_from']} to {registrer['currency_to']}",
                    "message": "Transacción exitosa"
                }
            ),HTTPStatus.CREATED 
        except sqlite3.Error as e:
            return jsonify(
                    {
                        "data": str(e),
                        "status": "Error"
                    }
                ),HTTPStatus.BAD_REQUEST
        
@app.route(f"/api/{VERSION}/status")
def get_info_status():
    try:
        euros_invested = get_inversion_total()
        euros_recovered = get_recovered_inversion()
        purchase_value = round((euros_invested - euros_recovered), 2)
        current_assets = get_cryptos_value()

        return jsonify(
            {
            'status' : 'success',
            'data' : {
            'invested': euros_invested,
            'recovered': euros_recovered,
            'purchase_value': purchase_value,
            'current_assets' : current_assets
            }
            }
        )
    except sqlite3.Error as e:
            return jsonify(
                    {
                        "data": str(e),
                        "status": "fail"
                    }
                ),HTTPStatus.BAD_REQUEST