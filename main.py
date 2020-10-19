from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'succsess': '1', 'items' : [{'id':'1', 'name':'test'},{'id':'2', 'name':'test 2'}], 'total':'2'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)