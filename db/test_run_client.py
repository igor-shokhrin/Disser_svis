#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from flask import jsonify

# GET
# get_dictToSend = {'cmd': 'get_column_from_table', 'table': 'passes', 'resource_id': 'Name'}  # Get value from table
# get_dictToSend = {'cmd': 'get_value_from_table', 'table': 'passes', 'resource_id': 'Name', 'resource_data': 'Kir9'}  # Get value from table
get_dictToSend = {'cmd': 'get_data_from_table', 'table': 'passes'}  # Get all data from table
# get_dictToSend = {'cmd': 'get_tables'}  # Get table names
# get_dictToSend = {'cmd': 'get_column_name_from_table', 'table': 'passes'}  # Get column name from table
# get_dictToSend = {'cmd': 'help', 'cmd_name': 'get_tables'}  # Get command help
# POST
post_dictToSend = {'cmd': 'add_value_to_table', 'table': 'passes', 'data': '[Arnold, Pupkin, A364AB33, 12.1.2019, 12.2.2019, 6, 4]'}  # Add data to table passes
# post_dictToSend = {'cmd': 'update_value_in_table', 'table': 'passes', 'resource_id': 'Name', 'resource_data': 'Kir9', 'param_column': 'Department_id', 'param_val': 3}  # Update value in table
# post_dictToSend = {'cmd': 'delete_value_from_table', 'table': 'passes', 'resource_id': 'Department_id', 'resource_data': 6}  # Get value from table
# post_dictToSend = {'cmd': 'help', 'cmd_name': 'all'}  # Get command help

ip = '127.0.0.1'
res = requests.post('http://'+ip+':5000/api', json=post_dictToSend) # add_val, update_val, delete_val
# res = requests.post('http://192.168.43.33:5000/tests/endpoint', json=dictToSend)
print('response from server:', res.text)
# dictFromServer = res.json()
res = requests.get('http://'+ip+':5000/api', json=get_dictToSend) # get_val, get_data, get_tables, get_column_name
# res = requests.post('http://192.168.43.33:5000/tests/endpoint', json=dictToSend)
print('response from server:', res.text)

# add_val // table data
# update val // table id_column record_id, param_colomn param_val
# get_val // table resource_id, resource_data
# get_data // table
# delete_val // table resource_id, resource_data
# get_tables // nothing
# get_column_name // table
# help cmd_name
