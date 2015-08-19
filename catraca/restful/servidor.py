#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

"""Implementacao de servidor REST utilizando Flask RESTful."""


from flask import Flask, jsonify, abort, make_response
from flask.ext.restful import Api, Resource, reqparse, fields, marshal, marshal_with_field
from flask.ext.httpauth import HTTPBasicAuth
import json
import decimal, simplejson

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
    return make_response(jsonify({'message': 'Acesso negado.'}), 403)

tipo = TipoDAO().busca(1)

#print json.dumps(tipo.__dict__ ,default=decimal_default,sort_keys=True,indent=4,separators=(',', ': '))

class DecimalJSONEncoder(simplejson.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalJSONEncoder, self).default(o)

#tasks = json.dumps(tipo.__dict__, sort_keys=True, indent=4, cls=DecimalJSONEncoder)
tasks = simplejson.dumps(tipo.__dict__, sort_keys=True, indent=4)


print tasks

# tasks_teste = [
#  
#     {
#         '_Tipo__tipo_id': 1,
#         '_Tipo__tipo_nome': "TESTE",
#         '_Tipo__tipo_vlr_credito': 1.10
#     }
# ]
#  
# print tasks_teste
 
#tasks = tasks_teste

#tasks = json.dumps(tipo.__dict__,use_decimal=True)

# tasks = json.dumps(tipo, skipkeys=False, ensure_ascii=True, 
#            check_circular=True, allow_nan=True, cls=None, 
#            indent=None, separators=None, encoding='utf-8', 
#            default=None, **kw)

# tasks = [
#     {
#         'id': 1,
#         'title': u'teste 1',
#         'description': u'UM, DOIS, TR�S, QUATRO, CINCO.',
#         'done': False
#     },
#     {
#         'id': 2,
#         'title': u'Teste 02',
#         'description': u'1� teste com WebService RESTful.',
#         'done': False
#     },
#     {
#         'id': 3,
#         'title': str(tipo.nome),
#         'description': str(tipo.valor),
#         'done': False
#     }
# ]

# task_fields = {
#     'title': fields.String,
#     'description': fields.String,
#     'done': fields.Boolean,
#     'uri': fields.Url('task')
# }

task_fields = {
    '_Tipo__tipo_id': fields.Integer,
    '_Tipo__tipo_nome': fields.String,
    '_Tipo__tipo_vlr_credito': fields.Float,
    'uri': fields.Url('task')

}

# task_fields = {
#     '_Tipo__tipo_id': fields.Integer,
#     '_Tipo__tipo_nome': fields.String,
#     '_Tipo__tipo_vlr_credito': fields.Float,
#     'uri': fields.Url('task')
# }


class TaskListAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        #self.reqparse.add_argument('_Tipo__tipo_id', type=str, default="", location='json')
        #self.reqparse.add_argument('_Tipo__tipo_nome', type=str, required=True, help='Sem nome fornecido.', location='json')
        #self.reqparse.add_argument('_Tipo__tipo_vlr_credito', type=str, default="", location='json')
        super(TaskListAPI, self).__init__()

    @marshal_with_field(fields.List(fields.Integer))
    def get(self):
        print {'tasks': [marshal(task, task_fields) for task in tasks]}
        return {'tasks': [marshal(task, task_fields) for task in tasks]}
 
    def post(self):
        args = self.reqparse.parse_args()
        task = {
            #'id': tasks[-1]['id'] + 1,
            'id': tasks['id'],
            'nome': args['nome'],
            'valor': args['valor']#,
            #'done': False
        }
        tasks.append(task)
        return {'task': marshal(task, task_fields)}, 201


class TaskAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        #self.reqparse.add_argument('_Tipo__tipo_nome', type=str, location='json')
        #self.reqparse.add_argument('_Tipo__tipo_vlr_credito', type=str, location='json')
        #self.reqparse.add_argument('done', type=bool, location='json')
        super(TaskAPI, self).__init__()

    def get(self, id):
        task = [task for task in tasks if task['id'] == id]
        if len(task) == 0:
            abort(404)
        print {'task': marshal(task[0], task_fields)}
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


api.add_resource(TaskListAPI, '/api/catraca', endpoint='tasks')
api.add_resource(TaskAPI, '/api/catraca/<int:id>', endpoint='task')


if __name__ == '__main__':
    app.run(host='192.168.1.253', port=8089, debug=True)
