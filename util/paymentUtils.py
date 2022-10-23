from flask import request
from util.utils import get_db_connection


def get_Payment():
    conn = get_db_connection()
    cur = conn.cursor()  # creating a cursor

    if request.method == "GET":
        cur.execute('''SELECT "transactionId", "flightId", "individualPaymentId", "baseFare", "convenienceFee"
        FROM dbo."Payment";''')
        rows = cur.fetchall()
        conn.close()
        return rows


def create_Payment(data: dict):
    pass


def delete_Payment(data: dict):
    pass


def update_Payment(data: dict):
    pass
