#--------------------------------------------------------------------------------------------
#  Copyright (c) Red Hat, Inc. All rights reserved.
#  Licensed under the MIT License. See LICENSE in the project root for license information.
#--------------------------------------------------------------------------------------------

# This program prints Hello, world!

#str = 'python program'
#print('This is Sample, ' + str + '!')
from flask import Flask, request
#from flask_restful import Resource, Api
from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)
# api = Api(app)

app.config['MONGO_DBNAME'] = 'taskdb'
app.config['MONGO_URI'] = 'mongodb+srv://'

mongo = PyMongo(app)

@app.route('/task', methods=['GET'])
def get_all_stars():
  task = mongo.db.tasks
  output = []
  for t in task.find():
    output.append({'name' : t['name'], 'status' : t['status']})
  return jsonify({'result' : output})

@app.route('/singletask/', methods=['GET'])
def get_one_task(name):
  task = mongo.db.tasks
  t = task.find_one({'name' : name})
  if t:
    output = {'name' : t['name'], 'status' : t['status']}
  else:
    output = "No such task"
  return jsonify({'result' : output})

@app.route('/addtask', methods=['POST'])
def add_task():
  task = mongo.db.tasks
  name = request.json['name']
  status = request.json['status']
  task_id = task.insert({'name': name, 'status': status})
  new_task = task.find_one({'_id': task_id })
  output = {'name' : new_task['name'], 'status' : new_task['status']}
  return jsonify({'result' : output})

# class Greeting (Resource):
#     def get(self):
#         return 'This is a sample task service'

# api.add_resource(Greeting, '/') # Route_1

if __name__ == '__main__':
    app.run('0.0.0.0','3333')
