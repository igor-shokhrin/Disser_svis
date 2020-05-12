#!/usr/bin/env python
# -*- coding: utf-8 -*-

from recognition.resource_rcgn import ApiResource
from flask_restful import Api
from flask import Flask

app = Flask(__name__)
api = Api(app)


if __name__ == '__main__':
    api.add_resource(ApiResource, '/api_rcgn')
    app.run(debug=True, port="7000")