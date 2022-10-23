import uuid
from datetime import datetime

import psycopg2
from flask import request
from constants.constants import databaseName, dbUser, dbPassword, dbHost, dbPort, adminUserID


def get_UserAddress():
    conn = psycopg2.connect(database=databaseName, user=dbUser, password=dbPassword,
                            host=dbHost, port=dbPort)
    cur = conn.cursor()  # creating a cursor

    if request.method == "GET":
        # SELECT "addressId", "userId", "addressLine1", "addressLine2", city, state, "pinCode", "createdBy",
        # "createdDate", "updatedBy", "updatedDate" FROM dbo."UserAddress";
        cur.execute('SELECT * FROM dbo."UserAddress"')
        rows = cur.fetchall()
        conn.close()
        return rows


def create_UserAddress(data: dict):
    pass


def delete_UserAddress(data: dict):
    pass


def update_UserAddress(data: dict):
    pass
