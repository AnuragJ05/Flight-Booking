from flask import Flask, request, jsonify
import util.userUtils
from util.UserAddressUtils import get_UserAddress
from util.UserBookingPassengerUtils import get_UserBookingPassenger
from util.UserBookingTransactionUtils import get_UserBookingTransaction
from util.UserBookingsUtils import get_UserBookings
from util.UserPassengerDetailsUtils import get_UserPassengerDetails
from util.UserPasswordEntityUtils import get_UserPasswordEntity
from util.bookingItenraryUtils import get_BookingItenrary
from util.flightUtils import get_flight_details
from util.paymentUtils import get_Payment
from util.utils import insert_new_user, get_db_connection, check_passwd

app = Flask(__name__)
form_data = None


@app.route('/user', methods=["Get", "Post", "DELETE"])
def user():
    if request.method == "GET":
        """
        Get : http://localhost:5050/user
        """
        rows = util.userUtils.get_users()
        return rows

    elif request.method == "POST":
        """
        Post : http://localhost:5050/user
        {
            "username": "test1234",
            "firstName": "test2",
            "middleName": "test2",
            "lastName": "test2",
            "DOB": "05/11/2000",
            "mobileNo": "0999675302"
        }
        """
        data = util.userUtils.create_user(data=request.json)
        return data
    elif request.method == "DELETE":
        """
        Delete : http://localhost:5050/user
        {
            "username": "test1234"
        }
        """
        data = util.userUtils.delete_user(data=request.json)
        return data


@app.route('/payment', methods=["Get"])
def payment():
    if request.method == "GET":
        """
        Get : http://localhost:5050/payment
        """
        rows = get_Payment()
        return rows


@app.route('/bookingItenrary', methods=["Get"])
def booking_itenrary():
    if request.method == "GET":
        """
        Get : http://localhost:5050/bookingItenrary
        """
        rows = get_BookingItenrary()
        return rows


@app.route('/userAddress', methods=["Get"])
def user_address():
    if request.method == "GET":
        """
        Get : http://localhost:5050/userAddress
        """
        rows = get_UserAddress()
        return rows


@app.route('/userBookingPassenger', methods=["Get"])
def user_booking_passenger():
    if request.method == "GET":
        """
        Get : http://localhost:5050/userBookingPassenger
        """
        rows = get_UserBookingPassenger()
        return rows


@app.route('/userBookings', methods=["Get"])
def user_bookings():
    if request.method == "GET":
        """
        Get : http://localhost:5050/userBookings
        """
        rows = get_UserBookings()
        return rows


@app.route('/userBookingTransaction', methods=["Get"])
def user_booking_transaction():
    if request.method == "GET":
        """
        Get : http://localhost:5050/userBookingTransaction
        """
        rows = get_UserBookingTransaction()
        return rows


@app.route('/userPassengerDetails', methods=["Get"])
def user_passenger_details():
    if request.method == "GET":
        """
        Get : http://localhost:5050/userPassengerDetails
        """
        rows = get_UserPassengerDetails()
        return rows


@app.route('/userPasswordEntity', methods=["Get"])
def user_password_entity():
    if request.method == "GET":
        """
        Get : http://localhost:5050/userPasswordEntity
        """
        rows = get_UserPasswordEntity()
        return rows


@app.route('/flight', methods=["Get"])
def flight():
    if request.method == "GET":
        """
        Get : http://localhost:5050/flight
        """
        data = get_flight_details()
        return data


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
            check = check_passwd(user_name, passwd)


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
                if check:
                    return jsonify({"success": True})
            else:
                return jsonify({"username_exist": True})

        else:
            return jsonify({"invalid_requst": True})
    except Exception as e:
        print("Error in register {}".format(e))


if __name__ == '__main__':
    # Default 127.0.0.1:5000
    app.run(host="127.0.0.1", port=5050)
