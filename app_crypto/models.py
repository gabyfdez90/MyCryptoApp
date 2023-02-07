from app_crypto.connection import Connection
import requests
from config import COINAPI_KEY

def select_all():
    """
    Returns the values to fill in the transactions's table.
    """

    conn = Connection('SELECT date, time, currency_from, quantity_from, currency_to, quantity_to FROM transactions ORDER BY date;')
    rows = conn.res.fetchall()
    columns = conn.res.description

    transactions = []

    for row in rows:
        registry = {}
        position= 0

        for field in columns:
            registry[field[0]] = row[position]
            position += 1
        
        transactions.append(registry)

    conn.con.close()
    return transactions
    

def get_transaction_rate(currency_from, currency_to):
    """
    Get from CoinAPi.io the current transaction rate between two currencies.
    """

    r = requests.get(f"https://rest.coinapi.io/v1/exchangerate/{currency_from}/{currency_to}?apikey={COINAPI_KEY}")

    transaction_json = r.json()
    print(transaction_json)

    if r.status_code == 200:
        return transaction_json['rate']
    else:
        return "Ocurrió un error"


def calculate_currency_amount(crypto):
    """
    Determine the total amount of each currency in our portfolio.
    """

    obtained_amount = Connection("SELECT SUM(quantity_to) FROM transactions WHERE currency_to=?", (crypto,))
    obtained_amount = obtained_amount.res.fetchone()

    spent_amount = Connection("SELECT SUM(quantity_from) FROM transactions WHERE currency_from=?", (crypto,))
    spent_amount = spent_amount.res.fetchone()

    if obtained_amount:
        obtained_amount = obtained_amount[0]
    if obtained_amount == None:
        obtained_amount = 0

    if spent_amount:
        spent_amount = spent_amount[0]
    if spent_amount == None:
        spent_amount = 0

    #Here was the issue with NoneType values

    actual_amount = obtained_amount - spent_amount
    
    return actual_amount

def apply_exchange(currency_from, currency_to):
    """
    Determine if the trade action could be performed and its exchange rate.
    """
    currency_amount = calculate_currency_amount(currency_from)

    if currency_from != "EUR":
        if get_transaction_rate(currency_from, currency_to) >= currency_amount:
            return get_transaction_rate(currency_from, currency_to)
        else:
            return "No puede realizar este tradeo"
    else:
        return get_transaction_rate(currency_from, currency_to)
    

def insert(movement):
    """
    Adds to the database the row that cames from the frontend through an API.
    """
    connectInsert = Connection("INSERT INTO transactions(date,time,currency_from, quantity_from, currency_to, quantity_to) values(?,?,?,?,?,?)",movement)
    connectInsert.con.commit()
    connectInsert.con.close()