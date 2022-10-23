import uuid
from datetime import datetime

import psycopg2
from flask import request
from constants.constants import databaseName, dbUser, dbPassword, dbHost, dbPort, adminUserID


def get_BookingItenrary():
    conn = psycopg2.connect(database=databaseName, user=dbUser, password=dbPassword,
                            host=dbHost, port=dbPort)
    cur = conn.cursor()  # creating a cursor

    if request.method == "GET":
        # SELECT "itenraryId", "bookingId", "PNR", "from", "to", "travelDate", "departureTime", "arrivalTime",
        # "journeyType", "travelClass", "airlineVendor", "flightNo", "flightType", "baseFare" FROM
        # dbo."BookingItenrary";
        cur.execute('SELECT * FROM dbo."BookingItenrary"')
        rows = cur.fetchall()
        conn.close()
        return rows


def create_BookingItenrary(data: dict):
    pass


def delete_BookingItenrary(data: dict):
    pass


def update_BookingItenrary(data: dict):
    pass
