import uuid
from datetime import datetime
from flask import request
from constants.constants import adminUserID
from util.utils import get_db_connection


def get_users():
    conn = get_db_connection()
    cur = conn.cursor()  # creating a cursor

    if request.method == "GET":
        cur.execute('''SELECT "userId", username, "firstName", "middleName", "lastName", "DOB",
        "mobileNo", "createdBy",
        "createdDate", "updatedBy", "updatedDate" FROM dbo."User";''')
        rows = cur.fetchall()
        conn.close()
        return rows


def create_user(data: dict):
    conn = get_db_connection()
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
    conn = get_db_connection()
    cur = conn.cursor()  # creating a cursor

    # DELETE FROM dbo."User"
    # 	WHERE <condition>;
    userName = data["username"]
    cur.execute('''DELETE FROM dbo."User" WHERE username=\'{}\';'''.format(userName))
    conn.commit()
    conn.close()
    return {"Message": "{} user deleted".format(userName)}


def update_user(data: dict):
    conn = get_db_connection()
    cur = conn.cursor()  # creating a cursor

    if "userId" not in data:
        return "userId not provided"

    querylist = []
    for key in data:
        querylist.append("\"{}\"=\'{}\'".format(key, data[key]))
    queryString = ",".join(querylist)
    query = "UPDATE dbo.\"User\" \nSET {} where \"userId\"=\'{}\';".format(queryString, data["userId"])
    cur.execute(query)
    conn.commit()
    conn.close()
    return data
