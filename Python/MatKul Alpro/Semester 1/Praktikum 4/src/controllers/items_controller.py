import sqlite3

class ItemsController:
    conn = None

    def __init__(self):
        self.conn = sqlite3.connect('aqils.db')
        
    def createTable(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS product
             (date text, trans text, symbol text, qty real, price real)''')

