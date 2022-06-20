from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello World'}

    def post(self):
        return {'message': 'This is message from Post'}

    def put(self):
        return {'message': 'This is message from Put'}

    def delete(self):
        return {'message': 'This is message from Delete'}

api.add_resource(HelloWorld,'/greeting')

if __name__ == '__main__':
    app.run(debug=True)