from flask import request
from util.utils import get_db_connection


def get_UserBookingPassenger(passengerId):
    conn = get_db_connection()
    cur = conn.cursor()  # creating a cursor

    if request.method == "GET":
        cur.execute('''SELECT * 
        from dbo.\"BookingItenrary\" bi
        INNER JOIN dbo.\"UserBookings\" ub
        ON bi.\"bookingId\" = ub.\"bookingId\"
        INNER JOIN dbo.\"UserBookingPassenger\" ubp
        ON bi.\"bookingId\" = ubp.\"bookingId\"
        WHERE ubp.\"passengerId\"=\'{}\';
        '''.format(passengerId))
        result = cur.fetchall()
        columns = list(cur.description)
        # make dict
        results = []
        for row in result:
            row_dict = {}
            for i, col in enumerate(columns):
                row_dict[col.name] = row[i]
            results.append(row_dict)
        conn.close()
        return results


def create_UserBookingPassenger(data: dict):
    conn = get_db_connection()
    cur = conn.cursor()  # creating a cursor

    # INSERT INTO dbo."UserBookingPassenger"(
    # 	id, "bookingId", "passengerId", "seatNo")
    # 	VALUES (?, ?, ?, ?);
    cur.execute('''INSERT INTO dbo."UserBookingPassenger"(
    id, "bookingId", "passengerId", "seatNo")
    VALUES (\'{}\', \'{}\', \'{}\', \'{}\');
    '''.format(data["id"], data["bookingId"], data["passengerId"], data["seatNo"]))
    conn.commit()
    conn.close()


def delete_UserBookingPassenger(data: dict):
    pass


def update_UserBookingPassenger(data: dict):
    pass
