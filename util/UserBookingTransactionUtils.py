import uuid
from datetime import datetime

import psycopg2
from flask import request
from constants.constants import databaseName, dbUser, dbPassword, dbHost, dbPort, adminUserID


def get_UserBookingTransaction():
    conn = psycopg2.connect(database=databaseName, user=dbUser, password=dbPassword,
                            host=dbHost, port=dbPort)
    cur = conn.cursor()  # creating a cursor

    if request.method == "GET":
        # SELECT "bookingId", "transactionId", "totalAmount", "CGST", "SGST", "serviceCharge", "grantTotal",
        # promocode, "promocodeAmount", "paymentType" FROM dbo."UserBookingTransaction";
        cur.execute('SELECT * FROM dbo."UserBookingTransaction"')
        rows = cur.fetchall()
        conn.close()
        return rows


def create_UserBookingTransaction(data: dict):
    pass


def delete_UserBookingTransaction(data: dict):
    pass


def update_UserBookingTransaction(data: dict):
    pass
