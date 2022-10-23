from flask import request
from util.utils import get_db_connection


def get_BookingItenrary():
    conn = get_db_connection()
    cur = conn.cursor()  # creating a cursor

    if request.method == "GET":

        cur.execute('''SELECT "itenraryId", "bookingId", "PNR", "from", "to", "travelDate", "departureTime", 
        "arrivalTime", "journeyType", "travelClass", "airlineVendor", "flightNo", "flightType", "baseFare" FROM
        dbo."BookingItenrary";''')
        rows = cur.fetchall()
        conn.close()
        return rows


def create_BookingItenrary(data: dict):
    pass


def delete_BookingItenrary(data: dict):
    pass


def update_BookingItenrary(data: dict):
    pass
