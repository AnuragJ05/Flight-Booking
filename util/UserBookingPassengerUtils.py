from flask import request
from util.utils import get_db_connection


def get_UserBookingPassenger():
    conn = get_db_connection()
    cur = conn.cursor()  # creating a cursor

    if request.method == "GET":

        cur.execute(''' SELECT id, "bookingId", "passengerId", "seatNo" FROM dbo."UserBookingPassenger";''')
        rows = cur.fetchall()
        conn.close()
        return rows


def create_UserBookingPassenger(data: dict):
    pass


def delete_UserBookingPassenger(data: dict):
    pass


def update_UserBookingPassenger(data: dict):
    pass
