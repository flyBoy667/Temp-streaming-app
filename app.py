from flask import Flask
from flask_restful import Api, abort, Resource, marshal_with, fields, reqparse

app = Flask(__name__)
api = Api(app)


temp_fields = {"temperature": fields.String, "timestamp": fields.DateTime}

temp_args = reqparse.RequestParser()
temp_args.add_argument("temperature", type=float, required=True)
temp_args.add_argument("timestamp", type=str, required=True)


class Temperatures(Resource):
    @marshal_with(temp_fields)
    def get(self):
        return {"temperature": 25}

    def post(self):
        args = temp_args.parse_args()
        return {"message": "posting"}


api.add_resource(Temperatures, "/temp")


@app.route("/")
def index():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
