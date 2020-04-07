#!/usr/bin/env python
# -*- coding: utf-8 -*-

import test_sqlite_db as db_server
from test_resource import ApiResource
from flask_restful import Api
from flask import Flask, render_template, request, url_for, jsonify

app = Flask(__name__)
api = Api(app)


if __name__ == '__main__':
    api.add_resource(ApiResource, '/api')
    app.run(debug=True)