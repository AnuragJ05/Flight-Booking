import uuid
from datetime import datetime

import psycopg2
from flask import request
from constants.constants import databaseName, dbUser, dbPassword, dbHost, dbPort, adminUserID


def get_users():
    conn = psycopg2.connect(database=databaseName, user=dbUser, password=dbPassword,
                            host=dbHost, port=dbPort)
    cur = conn.cursor()  # creating a cursor

    if request.method == "GET":

        cur.execute('''SELECT "userId", username, "firstName", "middleName", "lastName", "DOB",
        "mobileNo", "createdBy",
        "createdDate", "updatedBy", "updatedDate" FROM dbo."User";''')
        rows = cur.fetchall()
        conn.close()
        return rows


def create_user(data: dict):
    conn = psycopg2.connect(database=databaseName, user=dbUser, password=dbPassword,
                            host=dbHost, port=dbPort)
    cur = conn.cursor()  # creating a cursor

    # INSERT INTO dbo."User"( "userId", username, "firstName", "middleName", "lastName", "DOB", "mobileNo",
    # "createdBy", "createdDate", "updatedBy", "updatedDate") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    cur.execute('''INSERT INTO dbo."User"("userId",username, "firstName", "middleName", 
    "lastName", "DOB", "mobileNo","createdBy","createdDate")
    VALUES (\'{}\',\'{}\',\'{}\', \'{}\', \'{}\', \'{}\',\'{}\',
    \'{}\',\'{}\');
      '''.format(uuid.uuid4(), data["username"], data["firstName"], data["middleName"], data["lastName"],
                 data["DOB"], data["mobileNo"], adminUserID,
                 datetime.today().strftime('%d/%m/%y')))
    conn.commit()
    conn.close()
    return data


def delete_user(data: dict):
    conn = psycopg2.connect(database=databaseName, user=dbUser, password=dbPassword,
                            host=dbHost, port=dbPort)
    cur = conn.cursor()  # creating a cursor

    # DELETE FROM dbo."User"
    # 	WHERE <condition>;
    userName = data["username"]
    cur.execute('''DELETE FROM dbo."User" WHERE username=\'{}\';'''.format(userName))
    conn.commit()
    conn.close()
    return {"Message": "{} user deleted".format(userName)}


def update_user(data: dict):
    pass
