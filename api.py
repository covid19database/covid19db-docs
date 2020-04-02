"""
'Hello World' app, basically lol. Will add a reaaaalll db later.
Copy pasta from https://github.com/python-restx/flask-restx
"""

from flask import Flask
from flask_restx import Api, Resource, fields
from collections import defaultdict


app = Flask(__name__)
api = Api(app, version='1.0', title='TraceMVC API',
    description='A simple TraceMVC API',
)

ns = api.namespace('traces', description='Trace operations')

trace = api.model('Trace', {
    'plus_codes': fields.String(required=True, description='pluscod.es'),
    'unix_timestamp': fields.String(required=True, description='String representing Unix timestamp'),
    'domain': fields.String(required=True, description='Domain name'),
    'key': fields.String(required=True, description='String of map key'),
    'value': fields.String(required=True, description='String containing value'),
})

class TraceDAO(object):
    def __init__(self):
        self.counter = 0
        self.traces = []

    def get(self, id):
        for trace in self.traces:
            if trace['id'] == id:
                return trace
        api.abort(404, "Trace {} doesn't exist".format(id))

    def create(self, data):
        trace = data
        trace['id'] = self.counter = self.counter + 1
        self.traces.append(trace)
        return trace

    def update(self, id, data):
        trace = self.get(id)
        trace.update(data)
        return trace

    def delete(self, id):
        trace = self.get(id)
        self.traces.remove(trace)


DAO = TraceDAO()
DAO.create({'trace': 'Build an API'})
DAO.create({'trace': '?????'})
DAO.create({'trace': 'profit!'})


@ns.route('/')
class TraceList(Resource):
    '''Shows a list of all traces, and lets you POST to add new traces'''
    @ns.doc('list_traces')
    @ns.marshal_list_with(trace)
    def get(self):
        '''List all traces'''
        return DAO.traces

    @ns.doc('create_trace')
    @ns.expect(trace)
    @ns.marshal_with(trace, code=201)
    def post(self):
        '''Create a new trace'''
        return DAO.create(api.payload), 201


@ns.route('/<int:id>')
@ns.response(404, 'Trace not found')
@ns.param('id', 'The trace identifier')
class Trace(Resource):
    '''Show a single trace item and lets you delete them'''
    @ns.doc('get_trace')
    @ns.marshal_with(trace)
    def get(self, id):
        '''Fetch a given resource'''
        return DAO.get(id)

    @ns.doc('delete_trace')
    @ns.response(204, 'Trace deleted')
    def delete(self, id):
        '''Delete a trace given its identifier'''
        DAO.delete(id)
        return '', 204

    @ns.expect(trace)
    @ns.marshal_with(trace)
    def put(self, id):
        '''Update a trace given its identifier'''
        return DAO.update(id, api.payload)


if __name__ == '__main__':
    app.run(debug=True)
