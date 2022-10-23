import uuid
from datetime import datetime

import psycopg2
from flask import request
from constants.constants import databaseName, dbUser, dbPassword, dbHost, dbPort, adminUserID


def get_UserBookingPassenger():
    conn = psycopg2.connect(database=databaseName, user=dbUser, password=dbPassword,
                            host=dbHost, port=dbPort)
    cur = conn.cursor()  # creating a cursor

    if request.method == "GET":
        # SELECT id, "bookingId", "passengerId", "seatNo"
        # 	FROM dbo."UserBookingPassenger";
        cur.execute('SELECT * FROM dbo."UserBookingPassenger"')
        rows = cur.fetchall()
        conn.close()
        return rows


def create_UserBookingPassenger(data: dict):
    pass


def delete_UserBookingPassenger(data: dict):
    pass


def update_UserBookingPassenger(data: dict):
    pass
