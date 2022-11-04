from flask import request
from util.utils import get_db_connection


def get_UserPasswordEntity():
    conn = get_db_connection()
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
