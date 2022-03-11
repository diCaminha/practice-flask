from flask import Flask, request
from flask_restful import Resource, Api 

app = Flask(__name__)
api = Api(app)


items = []

class Student(Resource):
    def get(self, name):
        return {'student': name}

class Item(Resource):
    def get(self, name):
        print(items)
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self,name):
        data = request.get_json()
        items.append({'name': data['name'], 'price': data['price']})
        return data, 201

api.add_resource(Student, '/student/<string:name>')
api.add_resource(Item, '/item/<string:name>')

app.run(port=5000)
