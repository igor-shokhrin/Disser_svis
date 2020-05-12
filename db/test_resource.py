from flask import jsonify
from flask_restful import Resource, reqparse
from db import test_sqlite_db as req_db

parser = reqparse.RequestParser()
parser.add_argument('cmd', required=True)
parser.add_argument('table')
parser.add_argument('data')
parser.add_argument('cmd_name')
parser.add_argument('resource_id')
parser.add_argument('resource_data')
parser.add_argument('param_column')
parser.add_argument('param_val')

data_base = './db/test_data/1st_db_test.db'

supported_get_cmd = {"get_value_from_table":
                         {"usage": "{'cmd': 'get_value_from_table', 'table': 'passes', 'resource_id': 'Name', 'resource_data': 'Kir9'}",
                          "keys": ['table', 'resource_id', 'resource_data']},
                     "get_column_from_table":
                         {"usage": "{'cmd': 'get_value_from_table', 'table': 'passes', 'resource_id': 'Name'",
                          "keys": ['table', 'resource_id']},
                     "get_data_from_table":
                         {"usage": "{'cmd': 'get_data_from_table', 'table': 'passes'}",
                          "keys": ['table']},
                     "get_tables":
                         {"usage": "{'cmd': 'get_tables'}",
                          "keys": []},
                     "get_column_name_from_table":
                         {"usage": "{'cmd': 'get_column_name_from_table', 'table': 'passes'}",
                          "keys": ['table']},
                     "help":
                         {"usage": "{'cmd': 'help', 'cmd_name': 'get_tables'}",
                          "keys": ['cmd_name']},
                     "all":
                         {
                             "usage": "supported get commands: get_value_from_table, get_column_from_table, get_data_from_table, get_tables, get_column_name_from_table, help",
                             "keys": []}
                     }
supported_post_cmd = {"add_value_to_table":
                          {"usage": "{'cmd': 'add_value_to_table', 'table': 'passes', 'data': ['Uzziel', 'Gonzalez', 'A456AA777', '01.12.2019', '01.12.2020', 6, 4]}",
                           "keys": ['table', 'data']},
                      "update_value_in_table":
                          {"usage": "{'cmd': 'update_value_in_table', 'table': 'passes', 'resource_id': 'Name', 'resource_data': 'Kir9', 'param_column': 'Department_id', 'param_val': 3}",
                           "keys": ['table', 'resource_id', 'resource_data', 'param_column', 'param_val']},
                     "delete_value_from_table":
                          {"usage": "{'cmd': 'delete_value_from_table', 'table': 'passes', 'resource_id': 'Name', 'resource_data': 'Kir9'}",
                           "keys": ['table', 'resource_id', 'resource_data']},
                     "help":
                          {"usage": "{'cmd': 'help', 'cmd_name': 'all'}",
                           "keys": ['cmd_name']},
                     "all":
                        {"usage": "supported post commands add_value_to_table, update_value_in_table, delete_value_from_table, help",
                        "keys": []}
                      }


class ApiResource(Resource):
    def get(self):
        args = parser.parse_args()
        print(args)
        if(args["cmd"] not in supported_get_cmd.keys()):
            return jsonify({'response': "Invalid request. Use "+supported_get_cmd["help"]["usage"]})
        for key in supported_get_cmd[args["cmd"]]['keys']:
            if args[key]==None:
                return jsonify({'response': "Invalid request. Use " + supported_get_cmd["help"]["usage"]})

        if(args['cmd']=='get_value_from_table'):
            return jsonify({'response': req_db.get_value_from_table(data_base, args['table'], args['resource_id'], args['resource_data'])})

        if(args['cmd']=='get_column_from_table'):
            return jsonify({'response': req_db.read_data_from_table(data_base, args['table'], args['resource_id'])})

        if(args['cmd'] == 'get_data_from_table'):
            return jsonify({'response': req_db.read_data_from_table(data_base, args['table'])})

        if(args['cmd'] == 'get_tables'):
            return jsonify({'response': req_db.get_tables_name(data_base)})

        if(args['cmd'] == 'get_column_name_from_table'):
            return jsonify({'response': req_db.get_column_name_from_table(data_base, args['table'])})

        if(args['cmd'] == 'help'): return jsonify({'response': [["Usage:" + supported_get_cmd[args['cmd_name']]['usage']]]})
        print(args)
        return jsonify({'response': 'KY privet'})

    def post(self):
        args = parser.parse_args()
        if (args["cmd"] not in supported_post_cmd.keys()):
            return jsonify({'response': "Invalid request. Use " + supported_post_cmd["help"]["usage"]})
        for key in supported_post_cmd[args["cmd"]]['keys']:
            if args[key]==None:
                return jsonify({'response': "Invalid request. Use " + supported_post_cmd["help"]["usage"]})
        print(args)
        if(args['cmd']=='add_value_to_table'):
            req_db.add_data_in_table(data_base, args['table'], args['data'].strip('][').split(', '))
            jsonify({'response': args['cmd']+' is success'})
        if(args['cmd']=='update_value_in_table'):
            req_db.update_data_in_table(data_base, args['table'], args['resource_id'], args['resource_data'], args['param_column'], args['param_val'])
        if(args['cmd']=='delete_value_from_table'):
            req_db.delete_data_in_table(data_base, args['table'], args['resource_id'], args['resource_data'])
        if (args['cmd'] == 'help') :
            return jsonify({'response': [["Usage:" + supported_post_cmd[args['cmd_name']]['usage']]]})
        return jsonify({'response': 'OK'})


