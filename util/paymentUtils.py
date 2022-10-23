import uuid
from datetime import datetime

import psycopg2
from flask import request
from constants.constants import databaseName, dbUser, dbPassword, dbHost, dbPort, adminUserID


def get_Payment():
    conn = psycopg2.connect(database=databaseName, user=dbUser, password=dbPassword,
                            host=dbHost, port=dbPort)
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
