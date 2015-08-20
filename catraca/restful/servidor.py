#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

"""Implementacao de servidor REST utilizando Flask RESTful."""


from flask import Flask, jsonify, abort, make_response
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from flask.ext.httpauth import HTTPBasicAuth
from catraca.dao.tipodao import TipoDAO
from catraca.dao.tipo import Tipo
import json
import decimal, simplejson
#from catraca.dao.mensagemdao import MensagemDAO

app = Flask(__name__, static_url_path="")
api = Api(app)
auth = HTTPBasicAuth()

tipo = Tipo()
tipo_dao = TipoDAO()

@auth.get_password
def get_password(username):
    if username == 'catraca':
        return 'Unilab'
    return None


@auth.error_handler
def unauthorized():
    # retornar 403 em vez de 401 para impedir a exibicao padrao dos navegadores
    # auth dialog
    return make_response(jsonify({'message': 'Acesso negado.'}), 403)

class DecimalJSONEncoder(simplejson.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalJSONEncoder, self).default(o)
#     
# #tipo = MensagemDAO().busca()
# 
# #print json.dumps(tipo.__dict__ ,default=decimal_default,sort_keys=True,indent=4,separators=(',', ': '))
# #tasks = json.dumps(tipo.__dict__, sort_keys=True, indent=4, cls=DecimalJSONEncoder)
# #tasks = simplejson.dumps(tipo.__dict__, sort_keys=True, indent=4)

def obtem_lista(lista):
    ilista=[]
    for item in lista:
        i = {
            'id':item[0],
            'title':item[1],
            'description':item[2]
        }
        ilista.append(i)
    return ilista

# tasks = [
#     {
#         'id': 1,
#         'title': u'Buy groceries',
#         'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
#         'done': False
#      },
#     {
#         'id': 2,
#         'title': u'Learn Python',
#         'description': u'Need to find a good Python tutorial on the web',
#         'done': False
#     }
# ]
# 
# task_fields = {
#     'title': fields.String,
#     'description': fields.String,
#     'done': fields.Boolean,
#     'uri': fields.Url('task')
# }

tasks = obtem_lista(tipo_dao.busca())

print tasks

task_fields = {
    #'id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'done': fields.Boolean,
    'uri': fields.Url('task')
}


class TaskListAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, required=True, help='No task title provided', location='json')
        self.reqparse.add_argument('description', type=str, default="", location='json')
        super(TaskListAPI, self).__init__()


    def get(self):
        print "SELECIONOU"
        #return {'tasks': [marshal(task, task_fields) for task in tasks]}
        return {'tasks': map(lambda t: marshal(t, task_fields), tasks)}

    def post(self):
        args = self.reqparse.parse_args()
        task = {
            'id': tasks[-1]['id'] + 1,
            'title': args['title'],
            'description': args['description'],
            'done': False
        }
        #tasks.append(task)
        tipo = Tipo()
        tipo.nome = args['title']
        tipo.valor = args['description']
        tipo_dao.mantem(tipo,False)
        print tipo_dao.aviso
        tasks.append(task)
        print "INSERIU"
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
        print "SELECT"
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
                
#         tipo = Tipo()
#         tipo.nome = args['title']
#         tipo.valor = args['description']
#         tipo_dao.mantem(tipo,False)
#         print tipo_dao.aviso
                
        print "EDITOU"
        return {'task': marshal(task, task_fields)}

    def delete(self, id):
        task = [task for task in tasks if task['id'] == id]
        if len(task) == 0:
            abort(404)
        tasks.remove(task[0])
        print "EXCLUIU"
        return {'result': True}


api.add_resource(TaskListAPI, '/api/catraca', endpoint='tasks')
api.add_resource(TaskAPI, '/api/catraca/<int:id>', endpoint='task')

if __name__ == '__main__':
    app.run(debug=True)
