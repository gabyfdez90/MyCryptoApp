import sqlite3
from config import *


class Connection:
    def __init__(self, querySQL, params=[]):
        self.con = sqlite3.connect(ORIGIN_DATA)
        self.cur = self.con.cursor()
        self.res = self.cur.execute(querySQL, params)

    def fetchone(self):
        self.res = self.fetchone()