from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# class Employee(Resource):
#   def get(self, emp_id, name):
#      return {'emp_id ':emp_id, 'name ':name}

# api.add_resource(Employee,'/employee/<int:emp_id>/<string:name>')

emp_data_dict = \
    {
        100: {
            "name" : "Gaurav",
            "designation" : "Senior Engineer",
            "salary": 3232
        },
        200: {
            "name": "Pandey",
            "designation" : "Senior Devops Engineer",
            "salary": 232
        }
    }

class Employee(Resource):
    
    def get(self, emp_id):
        return emp_data_dict[emp_id]

api.add_resource(Employee, '/employee/<int:emp_id>')

if __name__ == '__main__':
    app.run(debug=True)
