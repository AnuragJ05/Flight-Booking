import uuid
from datetime import datetime

import psycopg2
from flask import request
from constants.constants import databaseName, dbUser, dbPassword, dbHost, dbPort, adminUserID


def get_UserPassengerDetails():
    conn = psycopg2.connect(database=databaseName, user=dbUser, password=dbPassword,
                            host=dbHost, port=dbPort)
    cur = conn.cursor()  # creating a cursor

    if request.method == "GET":
        cur.execute('''SELECT "passengerId", userid, "firstName", "middleName", "lastName", "DOB", 
        "mobileNo", "adhaarNo", "panCardNo" FROM dbo."UserPassengerDetails";''')
        rows = cur.fetchall()
        conn.close()
        return rows


def create_UserPassengerDetails(data: dict):
    pass


def delete_UserPassengerDetails(data: dict):
    pass


def update_UserPassengerDetails(data: dict):
    pass
