from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)

book_details = {}

class Book(Resource):

    def get(self, book_id):
        if book_id in book_details:
            return book_details[book_id]

        return {'message': 'Book with id: ' + book_id + 'not found'}

    def post(self, book_id):
        if book_id in book_details:
            return {'message': 'Book with id: ' + book_id + 'already exists'}

    # print('Details: ' + request.form["details"])
    # print('Author: ' + request.form["author"])
    # print('Tittle: ' + request.form["tittle"])
        book_info = {}
        for key in request.form:
            book_info[key] = request.form[key]

        book_details[book_id] = book_info

        return {'message': 'Book with id: ' + book_id + 'is added'}


api.add_resource(Book, '/books/<string:book_id>')
if __name__ == '__main__':
    app.run(debug=True)
