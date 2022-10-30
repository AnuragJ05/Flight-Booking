from base64 import encode
from re import T
from tkinter.tix import Tree
from turtle import pd
import uuid
import bcrypt
import psycopg2
from datetime import datetime
from constants.constants import databaseName, dbUser, dbPassword, dbHost, dbPort


def get_db_connection():
    conn = psycopg2.connect(host=dbHost,
                            port=dbPort,
                            database=databaseName,
                            user=dbUser,
                            password=dbPassword)
    conn.autocommit = False
    return conn


def get_password_from_db(user):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        query = (""" SELECT "usr"."userId", "usr"."username", "psswd"."userId", "psswd"."passwordHash" FROM dbo."User" usr join dbo."UserPasswordEntity" psswd on "usr"."userId" = "psswd"."userId" where "usr"."username" = '{}';""".format(user))
        cur.execute(query)
        a = cur.fetchall()

        return a[0][3]
    except Exception as e:
        print("Error in get_password_from_db {}".format(e))


def check_passwd(user_name, passwd):
    try:
        encryp_passwd = get_password_from_db(user_name)
        if bcrypt.checkpw(passwd.encode('utf8'), encryp_passwd.encode('utf8')):
            return True
        else:
            return False
    except Exception as e:
        print("Error in check passwd {}".format(e))


def insert_new_user(data):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        uid = uuid.uuid4()
        insert_query = ('''INSERT INTO dbo."User"
        ("userId", username, "firstName", "middleName",
        "lastName", "DOB", "mobileNo", "createdBy", "createdDate")
        VALUES 
        ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');'''.format(uid,
                                                                          data['username'], data['firstName'],
                                                                          data['middleName'], data['lastName'],
                                                                          data['DOB'],
                                                                          data['mobileNo'], uid, datetime.now()))
        # print(insert_query)
        cur.execute(insert_query)
        conn.commit()

        p_data = {"uid": uid, "password": data["password"]}

        check = insert_passwd(p_data)

        cur.close()
        conn.close()

        if check:
            return True

        return False
    except (Exception, psycopg2.Error) as error:
        print("Failed inserting record into user table {}".format(error))
        return False


def insert_passwd(data):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        pid = uuid.uuid4()
        p = data['password']
        encryt_p = bcrypt.hashpw(p.encode('utf8'), bcrypt.gensalt()).decode('utf8')
        insert_query = ('''INSERT INTO dbo."UserPasswordEntity"
        ("userPasswordId", "userId", "passwordHash", "otpSecret", "createdDate")
        VALUES 
        ('{}', '{}', '{}', '{}', '{}');'''.format(pid,
                                                  data['uid'], encryt_p, '', datetime.now()))
        print(insert_query)
        cur.execute(insert_query)
        conn.commit()
        cur.close()
        conn.close()
        return True
    except (Exception, psycopg2.Error) as error:
        print("Failed inserting record into password table {}".format(error))
        return False

# data = {}
# data['username'] = "akshay@bits.com" 
# data['firstName'] = "Akshay"
# data['middleName'] = "S"
# data['lastName'] = "Bhavsar"
# data['DOB'] = "06/03/1993"
# data['mobileNo'] = 8237355846 
# datetime.now()
