import imp
from flask import Flask, redirect, url_for, request, render_template, jsonify
import uuid
from datetime import datetime
from utils import *

# conn = psycopg2.connect(database="testdb", user = "postgres", password = "pass123", host = "127.0.0.1", port = "5432")
#
# print "Opened database successfully"
app = Flask(__name__)
form_data = None


@app.route('/user', methods=["Post", "Get"])
def get_user():
    conn = psycopg2.connect(database="Flight-Booking", user="postgres", password="0511", host="127.0.0.1", port="5432")

    print("Opened database successfully")
    cur = conn.cursor()  # creating a cursor

    if request.method == "GET":

        # SELECT "userId", username, "firstName", "middleName", "lastName", "DOB", "mobileNo", "createdBy",
        # "createdDate", "updatedBy", "updatedDate" FROM dbo."User";
        cur.execute('SELECT * FROM dbo."User"')
        rows = cur.fetchall()
        conn.close()
        return rows
    elif request.method == "POST":
        # INSERT INTO dbo."User"( "userId", username, "firstName", "middleName", "lastName", "DOB", "mobileNo",
        # "createdBy", "createdDate", "updatedBy", "updatedDate") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        cur.execute('''INSERT INTO dbo."User"("userId",username, "firstName", "middleName", 
        "lastName", "DOB", "mobileNo","createdBy","createdDate")
        VALUES (\'{}\',\'anurag05\',\'Anurag\', \'Jain\', \'Kumar\', \'1998-11-05\',\'0987654321\',
        \'a55b99a8-8182-459e-8b67-78abc73d5a06\',\'2022-10-16\');
          '''.format(uuid.uuid4()))
        conn.commit()
        conn.close()
        return {}


@app.route('/home', methods=["Post"])
def home():
    pass


@app.route('/', methods=["Post", "Get"])
def index():
    pass


@app.route("/login", methods=['POST'])
def user_login():
    try:
        if request.method == "POST" and "username" in request.data and "password" in request.data:
            user_name = request.data['username']
            passwd = request.data['password']
            
            check = check_passwd(user_name, )


    except Exception as e:
        print("Error in login {}".format(e))


@app.route("/register", methods=["POST"])
def register():
    try:
        if request.method == "POST" and "username" \
            in request.data and "password" in request.data:
            
            user_name = request.data['username']

            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("""SELECT * FROM dbo."User" WHERE username = '{}' """.format(user_name))
            exists = cur.fetchall()
            
            if not exists:
                check = insert_new_user(request.data)
                if check :
                    return jsonify({"success": True})
            else:
                return jsonify({"username_exist": True})

        else:
            return jsonify({"invalid_requst": True})
    except Exception as e:
        print("Error in register {}".format(e))


if __name__ == '__main__':
    # Default 127.0.0.1:5000
    app.run()
