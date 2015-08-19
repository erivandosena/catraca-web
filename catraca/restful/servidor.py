#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""Implementacao de servidor REST utilizando Flask RESTful."""


from flask import Flask, jsonify, abort, make_response
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from flask.ext.httpauth import HTTPBasicAuth

from catraca.dao.tipodao import TipoDAO


app = Flask(__name__, static_url_path="")
api = Api(app)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'catraca':
        return 'Unilab'
    return None


@auth.error_handler
def unauthorized():
    # retornar 403 em vez de 401 para impedir a exibicao padrao dos navegadores
    # auth dialog
    return make_response(jsonify({'message': 'Unauthorized access'}), 403)

tipo = TipoDAO().busca(1)
tasks = [
    {
        'id': 1,
        'title': u'teste 1',
        'description': u'UM, DOIS, TRÊS, QUATRO, CINCO.',
        'done': False
    },
    {
        'id': 2,
        'title': u'Teste 02',
        'description': u'1º teste com WebService RESTful.',
        'done': False
    },
    {
        'id': 3,
        'title': str(tipo.nome),
        'description': str(tipo.valor),
        'done': False
    }
]

task_fields = {
    'title': fields.String,
    'description': fields.String,
    'done': fields.Boolean,
    'uri': fields.Url('task')
}


class TaskListAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, required=True,
                                   help='No task title provided',
                                   location='json')
        self.reqparse.add_argument('description', type=str, default="",
                                   location='json')
        super(TaskListAPI, self).__init__()

    def get(self):
        return {'tasks': [marshal(task, task_fields) for task in tasks]}

    def post(self):
        args = self.reqparse.parse_args()
        task = {
            'id': tasks[-1]['id'] + 1,
            'title': args['title'],
            'description': args['description'],
            'done': False
        }
        tasks.append(task)
        return {'task': marshal(task, task_fields)}, 201


class TaskAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(TaskAPI, self).__init__()

    def get(self, id):
        task = [task for task in tasks if task['id'] == id]
        if len(task) == 0:
            abort(404)
        return {'task': marshal(task[0], task_fields)}

    def put(self, id):
        task = [task for task in tasks if task['id'] == id]
        if len(task) == 0:
            abort(404)
        task = task[0]
        args = self.reqparse.parse_args()
        for k, v in args.items():
            if v is not None:
                task[k] = v
        return {'task': marshal(task, task_fields)}

    def delete(self, id):
        task = [task for task in tasks if task['id'] == id]
        if len(task) == 0:
            abort(404)
        tasks.remove(task[0])
        return {'result': True}


api.add_resource(TaskListAPI, '/api/tasks', endpoint='tasks')
api.add_resource(TaskAPI, '/api/tasks/<int:id>', endpoint='task')


if __name__ == '__main__':
    app.run(host='192.168.1.253', port=8089, debug=True)
