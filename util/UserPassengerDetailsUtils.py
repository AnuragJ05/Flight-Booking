from flask import request
from util.utils import get_db_connection


def get_UserPassengerDetails():
    conn = get_db_connection()
    cur = conn.cursor()  # creating a cursor

    if request.method == "GET":
        cur.execute('''SELECT "passengerId", userid, "firstName", "middleName", "lastName", "DOB", 
        "mobileNo", "adhaarNo", "panCardNo" FROM dbo."UserPassengerDetails";''')
        rows = cur.fetchall()
        conn.close()
        return rows


def create_UserPassengerDetails(data: dict):
    conn = get_db_connection()
    cur = conn.cursor()  # creating a cursor

    # INSERT INTO dbo."UserPassengerDetails"(
    # 	"passengerId", userid, "firstName", "middleName", "lastName", "DOB", "mobileNo", "adhaarNo", "panCardNo")
    # 	VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    cur.execute('''INSERT INTO dbo."UserPassengerDetails"(
    "passengerId", userid, "firstName", "middleName", "lastName", "DOB", "mobileNo", "adhaarNo", "panCardNo")
    VALUES (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\');
              '''.format(data["passengerId"], data["userid"], data["firstName"], data["middleName"],
                         data["lastName"], data["DOB"], data["mobileNo"], data["adhaarNo"], data["panCardNo"]))
    conn.commit()
    conn.close()
    return data


def delete_UserPassengerDetails(data: dict):
    pass


def update_UserPassengerDetails(data: dict):
    pass
