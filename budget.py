import sqlite3
from datetime import datetime


class BudgetDB:
    def __init__(self, db_name='budget.db'):
        self.db_name = db_name
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS cash_table (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    bank_name TEXT NOT NULL,
                                    sum_of_money INTEGER NOT NULL,
                                    report_date TEXT NOT NULL
                                 )''')
            self.conn.execute('''CREATE TABLE IF NOT EXISTS credit_table (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    bank_name TEXT NOT NULL,
                                    credit_debt INTEGER NOT NULL,
                                    closest_payment_amount INTEGER NOT NULL,
                                    date_of_payment TEXT NOT NULL,
                                    report_date TEXT NOT NULL
                                 )''')

    def insert_cash(self, bank_name, sum_of_money, report_date=None):
        report_date = report_date or datetime.now().strftime('%Y-%m-%d')
        with self.conn:
            self.conn.execute('''INSERT INTO cash_table (bank_name, sum_of_money, report_date)
                                 VALUES (?, ?, ?)''', (bank_name, sum_of_money, report_date))

    def insert_credit(self, bank_name, credit_debt, closest_payment_amount, date_of_payment, report_date=None):
        report_date = report_date or datetime.now().strftime('%Y-%m-%d')
        with self.conn:
            self.conn.execute('''INSERT INTO credit_table (bank_name, credit_debt, closest_payment_amount, date_of_payment, report_date)
                                 VALUES (?, ?, ?, ?, ?)''', (bank_name, credit_debt, closest_payment_amount, date_of_payment, report_date))

    def close(self):
        if self.conn:
            self.conn.close()

# Example usage:
# if __name__ == "__main__":
#     db = BudgetDB()
#     db.connect()
#     db.insert_cash('Sber', 0, '2024-07-14')
#     db.insert_credit('Sber', 513970, 146043, '2024-07-31', '2024-07-14')
#     db.close()
