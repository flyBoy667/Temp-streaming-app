from flask import Flask
from flask_restful import Api, abort, Resource, marshal_with, fields

app = Flask(__name__)
api = Api(app)


temp_fiels = {
    "temperature": fields.String,
}


@app.route("/")
def index():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
