from config import *
from app_crypto.connection import Connection
from datetime import * 

def add_movement(values):
    connect_add = Connection(("insert into transactions(date,time,currency_from,quantity_from, currency_to, quantity_to) values(?,?,?)", values))
    connect_add.con.commit()
    connect_add.con.close()