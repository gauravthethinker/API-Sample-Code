from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

engg_emp_data_dict = \
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

sales_emp_data_dict = \
    {
        400: {
            "name" : "Nivedita",
            "designation" : "Senior sales VP",
            "salary": 323212
        },
        500: {
            "name": "Pandey",
            "designation" : "VP sales ",
            "salary": 23212
        }
    }

class EngineeringEmployee(Resource):
    def get(self, emp_id):
        return engg_emp_data_dict[emp_id]

class SalesEmployee(Resource):
    def get(self, emp_id):
        return sales_emp_data_dict[emp_id]

api.add_resource(EngineeringEmployee, '/eng/<int:emp_id>')
api.add_resource(SalesEmployee, '/sales/<int:emp_id>')

if __name__ == '__main__':
    app.run(debug=True)
