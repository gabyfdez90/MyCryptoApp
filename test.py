from app_crypto.models import *
from app_crypto.connection import Connection
from config import COINAPI_KEY


if __name__ == "__main__":

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

    return total_value

def get_recovered_inversion():
    """
    Returns the total of euros recovered through the app inversions.
    """

    con = Connection('SELECT SUM(quantity_to) FROM transactions WHERE currency_to = "EUR";')
    total_recovered = con.cur.fetchone()[0]
    con.con.close()

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
        print(rate)
        print(crypto_amount)
        crypto_value = rate * crypto_amount
        total_value += crypto_value

        total_value = round(total_value, 2)


amount = calculate_currency_amount("USDT")
print(amount)

# value = get_cryptos_value()
# print(value)

# euros = get_recovered_inversion()
# print(euros)

rate = get_transaction_rate("ETH", "EUR")
print(rate)