from flask import jsonify
from flask_restful import Resource, reqparse
from recognition.plate_recognize import plate_recognize


# 'python plate_recognition.py --api-key MY_API_KEY /path/to/vehicle-*.jpg\n'
parser = reqparse.RequestParser()
parser.add_argument('cmd', required=True)
parser.add_argument('api_key')
parser.add_argument('regions')
parser.add_argument('sdk_url')
parser.add_argument('camera_id')
parser.add_argument('path')
parser.add_argument('cmd_name')
parser.add_argument('mmc')



data_base = './test_data/1st_db_test.db'

supported_get_cmd = {"get_plate_from_image":
                         {"usage": "{'cmd': 'get_plate_from_image', 'path': '<path_to_image>'",
                          "keys": ['path']},
                     "help":
                         {"usage": "{'cmd': 'help', 'cmd_name': 'get_tables'}",
                          "keys": ['cmd_name']},
                     "all":
                         {
                             "usage": "supported get commands: get_value_from_table, get_column_from_table, get_data_from_table, get_tables, get_column_name_from_table, help",
                             "keys": []}
                     }
supported_post_cmd = {"add_value_to_table":
                          {"usage": "{'cmd': 'add_value_to_table', 'table': 'passes', 'data': ['Uzziel', 'Gonzalez', 6, 4]}",
                           "keys": ['table', 'data']},
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
        if(args['cmd'] == 'get_plate_from_image'):
            return jsonify({'response': plate_recognize(paths=args["path"].strip('][').split(', '))})
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
        if (args['cmd'] == 'help'):
            return jsonify({'response': [["Usage:" + supported_post_cmd[args['cmd_name']]['usage']]]})
        return jsonify({'response': 'OK'})


