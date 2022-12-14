import uuid
from datetime import datetime

from flask import Flask, request, jsonify
import util.userUtils
from constants.constants import adminUserID
from util.UserAddressUtils import get_UserAddress
from util.UserBookingPassengerUtils import get_UserBookingPassenger, create_UserBookingPassenger
from util.UserBookingTransactionUtils import get_UserBookingTransaction, create_UserBookingTransaction
from util.UserBookingsUtils import get_UserBookings, create_UserBookings
from util.UserPassengerDetailsUtils import get_UserPassengerDetails, create_UserPassengerDetails
from util.UserPasswordEntityUtils import get_UserPasswordEntity
from util.bookingItenraryUtils import get_BookingItenrary, create_BookingItenrary
from util.flightUtils import get_flight_details
from util.paymentUtils import get_Payment
from util.utils import insert_new_user, get_db_connection, check_passwd

app = Flask(__name__)
form_data = None


@app.route('/flight', methods=["Get"])
def flight():
    if request.method == "GET":
        """
        Get : http://localhost:5050/flight
        """
        data = get_flight_details()
        return data


@app.route('/passenger', methods=["Get", "Post"])
def passenger():
    if request.method == "GET":
        """
        Get : http://localhost:5050/passenger
        """
        rows = get_UserPassengerDetails()
        return rows

    elif request.method == "POST":
        """
        Post : http://localhost:5050/passenger
        {
            "firstName": "test2",
            "middleName": "test2",
            "lastName": "test2",
            "DOB": "05/11/2000",
            "mobileNo": "0999675302",
            "adhaarNo": 234582829191,
            "panCardNo" : "BI97B7V"
        }
        """
        data = request.json
        data["passengerId"] = uuid.uuid4()
        data["userid"] = adminUserID
        resp = create_UserPassengerDetails(data=data)

        return {"message": "passenger created successful!!"}


@app.route('/book', methods=["Get","Post"])
def book_flight():
    if request.method == "GET":
        """
        Get : http://localhost:5050/book?passengerId=cf093eed-27e9-46aa-a9c3-518dbc5892a3
        """
        args = request.args
        passengerId = args.get('passengerId')
        if not passengerId:
            return {"message": "Passenger ID not provided"}
        rows = get_UserBookingPassenger(passengerId)
        return rows
    elif request.method == "POST":
        """
        post: http://localhost:5050/book
        {
            "flight": {
                "PNR": "171515",
                "flightNo": "192837262",
                "flightType": "Charter",
                "airlineVendor": "US Airlines",
                "journeyType": "One-way",
                "travelClass": "First Class",
                "duration": 590,
                "travelDate": "2022-11-16",
                "departureTime": "2022-11-16T21:30",
                "arrivalTime": "2022-11-16T06:30",
                "from": "GRU",
                "to": "JFK",
                "baseFare": 8000
            },
            "passenger": [{
                "passengerId" : "cf093eed-27e9-46aa-a9c3-518dbc5892a3",
                "seatNo" : "34B"
            }],
            "payment" : {
                "totalAmount" : 8000,
                "CGST": 750,
                "SGST": 750,
                "serviceCharge" : 1000,
                "grantTotal" : 10500,
                "promocode" : "NA",
                "promocodeAmount" : 0,
                "paymentType": "CASH"
            }
        }
        """

        bookingId = uuid.uuid4()
        bookingDate = datetime.today().strftime('%d/%m/%y')
        booking_data = {
            "bookingId": bookingId,
            "bookingDate": bookingDate,
            "bookingStatus": "Done",
            "userid": adminUserID
        }
        create_UserBookings(booking_data)

        bookingItenary_data = request.json["flight"]
        bookingItenary_data["itenraryId"] = uuid.uuid4()
        bookingItenary_data["bookingId"] = bookingId
        create_BookingItenrary(bookingItenary_data)

        passenger_data = request.json["passenger"]
        for p_data in passenger_data:
            p_data["id"] = uuid.uuid4()
            p_data["bookingId"] = bookingId
            create_UserBookingPassenger(p_data)

        payment_data = request.json["payment"]
        payment_data["bookingId"] = bookingId
        payment_data["transactionId"] = uuid.uuid4()
        create_UserBookingTransaction(payment_data)

        return {"message": "booking successful!!"}


@app.route("/login", methods=['POST'])
def user_login():
    """
        Post : http://localhost:5050/login
        {
                "username": "dummy",
                "password": "12345678"
        }
        """
    try:
        if request.method == "POST" and "username" in request.json and "password" in request.json:
            user_name = request.json['username']
            passwd = request.json['password']
            check = check_passwd(user_name, passwd)
            if check:
                return jsonify({"login": True})
            else:
                return jsonify({"login": False})
    except Exception as e:
        print("Error in login {}".format(e))
        return jsonify({"login": False})


@app.route("/register", methods=["POST"])
def register():
    """
    Post : http://localhost:5050/register
    {
            "username": "dummy",
            "password": "12345678",
            "firstName": "dummy",
            "middleName": "dummy",
            "lastName": "dummy",
            "DOB": "05/11/1998",
            "mobileNo": "0999679302"
    }
    """
    try:
        print("data= ", request.json)
        if request.method == "POST" and "username" \
                in request.json and "password" in request.json:

            user_name = request.json['username']

            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("""SELECT * FROM dbo."User" WHERE username = \'{}\' """.format(user_name))
            exists = cur.fetchall()

            if not exists:
                check = insert_new_user(request.json)
                if check:
                    return jsonify({"success": True})
            else:
                return jsonify({"username_exist": True})

        else:
            return jsonify({"invalid_requst": True})
    except Exception as e:
        print("Error in register {}".format(e))


@app.route('/home', methods=["Post"])
def home():
    pass


@app.route('/', methods=["Post", "Get"])
def index():
    pass


if __name__ == '__main__':
    # Default 127.0.0.1:5000
    app.run(host="127.0.0.1", port=5050)
