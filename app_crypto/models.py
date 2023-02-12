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

    actual_amount = obtained_amount - spent_amount
    
    return actual_amount


def insert(movement):
    """
    Adds to the database the row that cames from the frontend through an API.
    """
    
    connectInsert = Connection("INSERT INTO transactions(date, time, currency_from, quantity_from, currency_to, quantity_to) values(?,?,?,?,?,?)",movement)
    connectInsert.con.commit()
    connectInsert.con.close()

def get_inversion_total():
    """
    Returns the total amount of euros invested in our crypto app
    """

    con = Connection('SELECT SUM(quantity_from) FROM transactions WHERE currency_from = "EUR";')
    total_invested = con.cur.fetchone()[0]
    con.con.close()

    return total_invested

def get_recovered_inversion():
    """
    Returns the total of euros recovered through the app inversions.
    """

    con = Connection('SELECT SUM(quantity_to) FROM transactions WHERE currency_to = "EUR";')
    total_recovered = con.cur.fetchone()[0]
    con.con.close()

    if total_recovered == None:
        total_recovered = 0

    total_recovered = round(total_recovered, 2)

    return total_recovered


def get_cryptos_value():
    """
    Obtain the current value of a all the cryptos in our wallet.
    """
    
    con = Connection('SELECT currency_to FROM transactions WHERE currency_to != "EUR";')
    active_cryptos = con.cur.fetchall()

    total_value = 0

    for crypto in active_cryptos:
        crypto = crypto[0]
        crypto_amount = calculate_currency_amount(crypto)
        rate = get_transaction_rate(crypto, "EUR")
        crypto_value = rate * crypto_amount
        total_value += crypto_value

        total_value = round(total_value, 2)

    return total_value
    
    
        