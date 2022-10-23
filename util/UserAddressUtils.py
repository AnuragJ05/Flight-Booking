from flask import request
from util.utils import get_db_connection


def get_UserAddress():
    conn = get_db_connection()
    cur = conn.cursor()  # creating a cursor

    if request.method == "GET":
        cur.execute('''SELECT "addressId", "userId", "addressLine1", "addressLine2", city, state, "pinCode", 
        "createdBy", "createdDate", "updatedBy", "updatedDate" FROM dbo."UserAddress";''')
        rows = cur.fetchall()
        conn.close()
        return rows


def create_UserAddress(data: dict):
    pass


def delete_UserAddress(data: dict):
    pass


def update_UserAddress(data: dict):
    pass
