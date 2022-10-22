from flask import Flask, request

from config.userConfig import get_users, create_user, delete_user

app = Flask(__name__)
form_data = None


@app.route('/user', methods=["Get", "Post", "DELETE"])
def user():
    if request.method == "GET":
        """
        Get : http://localhost:5050/user
        """
        rows = get_users()
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
        data = create_user(data=request.json)
        return data
    elif request.method == "DELETE":
        """
        Delete : http://localhost:5050/user
        {
            "username": "test1234"
        }
        """
        data = delete_user(data=request.json)
        return data


@app.route('/home', methods=["Post"])
def home():
    pass


@app.route('/', methods=["Post", "Get"])
def index():
    pass


if __name__ == '__main__':
    # Default 127.0.0.1:5000
    app.run(host="localhost", port=5050)
