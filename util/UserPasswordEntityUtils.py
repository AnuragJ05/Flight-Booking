import uuid
from datetime import datetime

import psycopg2
from flask import request
from constants.constants import databaseName, dbUser, dbPassword, dbHost, dbPort, adminUserID


def get_UserPasswordEntity():
    conn = psycopg2.connect(database=databaseName, user=dbUser, password=dbPassword,
                            host=dbHost, port=dbPort)
    cur = conn.cursor()  # creating a cursor

    if request.method == "GET":

        cur.execute('''SELECT "userPasswordId", "userId", "passwordHash", "otpSecret", 
        "createdDate" FROM dbo."UserPasswordEntity";''')
        rows = cur.fetchall()
        conn.close()
        return rows


def create_UserPasswordEntity(data: dict):
    pass


def delete_UserPasswordEntity(data: dict):
    pass


def update_UserPasswordEntity(data: dict):
    pass
