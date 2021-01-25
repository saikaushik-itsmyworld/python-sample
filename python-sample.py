#--------------------------------------------------------------------------------------------
#  Copyright (c) Red Hat, Inc. All rights reserved.
#  Licensed under the MIT License. See LICENSE in the project root for license information.
#--------------------------------------------------------------------------------------------

# This program prints Hello, world!

#str = 'python program'
#print('This is Sample, ' + str + '!')
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Greeting (Resource):
    def get(self):
        return 'This is a sample python service'

api.add_resource(Greeting, '/') # Route_1

if __name__ == '__main__':
    app.run('0.0.0.0','3333')