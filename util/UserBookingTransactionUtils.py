from flask import request
from util.utils import get_db_connection


def get_UserBookingTransaction():
    conn = get_db_connection()
    cur = conn.cursor()  # creating a cursor

    if request.method == "GET":
        cur.execute('''SELECT "bookingId", "transactionId", "totalAmount", "CGST", "SGST", "serviceCharge", 
        "grantTotal", promocode, "promocodeAmount", "paymentType" FROM dbo."UserBookingTransaction";''')
        rows = cur.fetchall()
        conn.close()
        return rows


def create_UserBookingTransaction(data: dict):
    pass


def delete_UserBookingTransaction(data: dict):
    pass


def update_UserBookingTransaction(data: dict):
    pass
