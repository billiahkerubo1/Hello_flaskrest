from flask import Flask
from flask_restx import Api
app = Flask(__name__)
api = Api(app, title='Toread API',
    description='A simple Toread API',
)
ns = api.namespace('todos', description='Books to read')

todo = api.model('Toread', {
    'id': fields.Integer(readonly=True, description='The book unique identifier'),
    'book': fields.String(required=True, description='The book details')
})


class ToreadDAO(object):
    def __init__(self):
        self.counter = 0
        self.toread = []

    def get(self, id):
        for todo in self.toread:
            if todo['id'] == id:
                return toread
        api.abort(404, "Toread {} doesn't exist".format(id))

    def create(self, data):
        toread = data
        toread['id'] = self.counter = self.counter + 1
        self.toread.append(todo)
        return todo

    def update(self, id, data):
        toread = self.get(id)
        toread.update(data)
        return toread

    def delete(self, id):
        todo = self.get(id)
        self.todos.remove(todo)


DAO = ToreadDAO()
DAO.create({'book': 'How to get away with murder'})
DAO.create({'book': '?????'})
DAO.create({'book': 'achievement!'})


@ns.route('/')
class ToreadList(Resource):
    '''Shows a list of all books to read, and lets you POST to add new books'''
    @ns.doc('list_toread')
    @ns.marshal_list_with(toread)
    def get(self):
        '''List all books'''
        return DAO.todos

    @ns.doc('create_toread')
    @ns.expect(toread)
    @ns.marshal_with(toread, code=201)
    def post(self):
        '''Create a new book'''
        return DAO.create(api.payload), 201


@ns.route('/<int:id>')
@ns.response(404, 'Toread not found')
@ns.param('id', 'The book identifier')
class Todo(Resource):
    '''Show a single toread item and lets you delete them'''
    @ns.doc('get_toread')
    @ns.marshal_with(toread)
    def get(self, id):
        '''Fetch a given resource'''
        return DAO.get(id)

    @ns.doc('delete_toread')
    @ns.response(204, 'Toread deleted')
    def delete(self, id):
        '''Delete a book given its identifier'''
        DAO.delete(id)
        return '', 204

    @ns.expect(toread)
    @ns.marshal_with(toread)
    def put(self, id):
        '''Update a book given its identifier'''
        return DAO.update(id, api.payload)


if __name__ == '__main__':
    app.run( host = "0.0.0.0", port = 5500, debug=True)