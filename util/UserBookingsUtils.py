import uuid
from datetime import datetime

import psycopg2
from flask import request
from constants.constants import databaseName, dbUser, dbPassword, dbHost, dbPort, adminUserID


def get_UserBookings():
    conn = psycopg2.connect(database=databaseName, user=dbUser, password=dbPassword,
                            host=dbHost, port=dbPort)
    cur = conn.cursor()  # creating a cursor

    if request.method == "GET":
        cur.execute('''SELECT "bookingId", userid, "bookingDate", "bookingStatus" FROM dbo."UserBookings";''')
        rows = cur.fetchall()
        conn.close()
        return rows


def create_UserBookings(data: dict):
    pass


def delete_UserBookings(data: dict):
    pass


def update_UserBookings(data: dict):
    pass
