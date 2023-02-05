from app_crypto.connection import Connection


def select_all():
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
    
