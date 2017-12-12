from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Get our config
app.config.from_object('config.DevelopmentConfig')

import ovh
client = ovh.Client(
    endpoint = app.config['ENDPOINT'],
    application_key = app.config['KEY'],
    application_secret = app.config['SECRET'],
    consumer_key = app.config['CONSUMER'],
)

class me(Resource):
    def get(self):
        statuses = client.get('/me')
        return statuses

class credz(Resource):
    def get(self):
        statuses = client.get('/auth/currentCredential')
        return statuses

class status(Resource):
    def get(self):
        statuses = client.get('/status/task')
        return statuses

class lb(Resource):
    def get(self,req=None):
        if req is None:
            lb = client.get('/ipLoadbalancing/%s/serviceInfos' % ( app.config['LBSERVICE'] ) )
            if "ok" in lb['status']:
                lb['lb_up'] = 1
            else:
                lb['lb_up'] = 0

        return lb

api.add_resource(me, '/me')
api.add_resource(credz, '/credz')
api.add_resource(status, '/status')
api.add_resource(lb, '/lb', '/lb/<req>')

