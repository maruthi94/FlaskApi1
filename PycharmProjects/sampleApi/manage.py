#!/usr/bin/env python
import os
import sys
from flask import Flask
from flask_restful import  Api , Resource

app = Flask(__name__)
api = Api(app)


class Foo(Resource):
        def get(self):
            return "hello", 200

        def post(self):
            pass


api.add_resource(Foo,'/')

if __name__ == "__main__":
    app.run(debug=True)





