from flask import request
from util.utils import get_db_connection


def get_UserBookings():
    conn = get_db_connection()
    cur = conn.cursor()  # creating a cursor

    if request.method == "GET":
        cur.execute('''SELECT "bookingId", userid, "bookingDate", "bookingStatus" FROM dbo."UserBookings";''')
        rows = cur.fetchall()
        conn.close()
        return rows


def create_UserBookings(data: dict):
    conn = get_db_connection()
    cur = conn.cursor()  # creating a cursor

    # INSERT INTO dbo."UserBookings"(
    # 	"bookingId", userid, "bookingDate", "bookingStatus")
    # 	VALUES (?, ?, ?, ?);
    cur.execute('''INSERT INTO dbo."UserBookings"(
    "bookingId", userid, "bookingDate", "bookingStatus")
    VALUES (\'{}\', \'{}\', \'{}\', \'{}\');
          '''.format(data["bookingId"], data["userid"], data["bookingDate"], data["bookingStatus"]))
    conn.commit()
    conn.close()


def delete_UserBookings(data: dict):
    pass


def update_UserBookings(data: dict):
    pass
