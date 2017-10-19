#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

"""Implementacao de servidor REST utilizando Flask RESTful."""

from flask import Flask, jsonify, abort, make_response
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from flask.ext.httpauth import HTTPBasicAuth

from catraca.dao.tipodao import TipoDAO
from catraca.dao.tipo import Tipo

from catraca.dao.registrodao import RegistroDAO
from catraca.dao.registro import Registro

from catraca.logs import Logs

app = Flask(__name__, static_url_path="")
api = Api(app)
auth = HTTPBasicAuth()

tipo_obj = Tipo()
tipo_dao = TipoDAO()

registro_obj = Registro()
registro_dao = RegistroDAO()


@auth.get_password
def get_password(username):
    if username == 'catraca':
        return 'Unilab'
    return None

@auth.error_handler
def unauthorized():
    # retornar 403 em vez de 401 para impedir a exibicao padrao dos navegadores
    return make_response(jsonify({'message': 'Acesso negado.'}), 403)

#####################################################################
## INICIO RECURSO TIPO
#####################################################################
def lista_tipos(lista):
    ilista=[]
    for item in lista:
        i = {
            'id':item[0],
            'nome':item[1],
            'valor':item[2]
        }
        ilista.append(i)
    return ilista

tipos = lista_tipos(tipo_dao.busca())

tipo_fields = {
    'nome': fields.String,
    'valor': fields.String,
    'uri': fields.Url('tipo')
}


class TipoListAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        #self.reqparse.add_argument('nome', type=str, required=True, help='Sem nome fornecido', location='json')
        #self.reqparse.add_argument('valor', type=str, default="", location='json')
        super(TipoListAPI, self).__init__()

    def get(self):
        print "SELECIONOU"
        #return {'tipos': [marshal(tipo, tipo_fields) for tipo in tipos]}
        return {'tipos': map(lambda t: marshal(t, tipo_fields), tipos)}

    def post(self):
        args = self.reqparse.parse_args()
        tipo = {
            'id': tipos[-1]['id'] + 1,
            'nome': args['nome'],
            'valor': args['valor']
        }
        #tipos.append(tipo)
        #tipo = Tipo()
        tipo_obj.nome = args['nome']
        tipo_obj.valor = args['valor']
        tipo_dao.mantem(tipo_obj,False)
        print tipo_dao.aviso
        tipos.append(tipo)
        print "INSERIU"
        return {'tipo': marshal(tipo, tipo_fields)}, 201


class TipoAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('nome', type=str, location='json')
        self.reqparse.add_argument('valor', type=str, location='json')
        super(TipoAPI, self).__init__()

    def get(self, id):
        tipo = [tipo for tipo in tipos if tipo['id'] == id]
        if len(tipo) == 0:
            abort(404)
        print "SELECT"
        return {'tipo': marshal(tipo[0], tipo_fields)}

    def put(self, id):
        tipo = [tipo for tipo in tipos if tipo['id'] == id]
        if len(tipo) == 0:
            abort(404)
        tipo = tipo[0]
        args = self.reqparse.parse_args()
        for k, v in args.items():
            if v is not None:
                tipo[k] = v
                
        tipo_obj = tipo_dao.busca(id)
        tipo_obj.nome = args['nome']
        tipo_obj.valor = args['valor']
        tipo_dao.mantem(tipo_obj,False)
        print tipo_dao.aviso
                
        print "EDITOU"
        return {'tipo': marshal(tipo, tipo_fields)}

    def delete(self, id):
        tipo = [tipo for tipo in tipos if tipo['id'] == id]
        if len(tipo) == 0:
            abort(404)
            
        tipo_obj = tipo_dao.busca(id)
        tipo_dao.mantem(tipo_obj,True)
        print tipo_dao.aviso
            
        tipos.remove(tipo[0])
        print "EXCLUIU"
        return {'result': True}

api.add_resource(TipoListAPI, '/api/catraca/tipos', endpoint='tipos')
api.add_resource(TipoAPI, '/api/catraca/tipos/<int:id>', endpoint='tipo')
#####################################################################
## FIM RECURSO TIPO
##################################################################### 

#####################################################################
## INICIO RECURSO REGISTRO
#####################################################################
def lista_registros(lista):
    ilista=[]
    for item in lista:
        i = {
            'id':item[0],
            'data':item[1],
            'giro':item[2],
            'valor':item[3],
            'cartao':item[4]
        }
        ilista.append(i)
    return ilista

registros = lista_registros(registro_dao.busca())

registro_fields = {
    'data': fields.String,
    'giro': fields.String,
    'valor': fields.String,
    'cartao': fields.String,
    'uri': fields.Url('registro')
}


class RegistroListAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        #self.reqparse.add_argument('cartao', type=str, required=True, help='Sem nome fornecido', location='json')
        #self.reqparse.add_argument('valor', type=str, default="", location='json')
        super(RegistroListAPI, self).__init__()

    def get(self):
        print "SELECIONOU"
        #return {'registros': [marshal(registro, registro_fields) for registro in registros]}
        return {'registros': map(lambda t: marshal(t, registro_fields), registros)}

    def post(self):
        args = self.reqparse.parse_args()
        registro = {
            'id': registros[-1]['id'] + 1,
            'nome': args['nome'],
            'valor': args['valor']
        }
        #registros.append(registro)
        #registro = Registro()
        registro_obj.nome = args['nome']
        registro_obj.valor = args['valor']
        registro_dao.mantem(registro_obj,False)
        print registro_dao.aviso
        registros.append(registro)
        print "INSERIU"
        return {'registro': marshal(registro, registro_fields)}, 201


class RegistroAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('data', type=str, location='json')
        self.reqparse.add_argument('giro', type=str, location='json')
        self.reqparse.add_argument('valor', type=str, location='json')
        self.reqparse.add_argument('cartao', type=str, location='json')
        super(RegistroAPI, self).__init__()

    def get(self, id):
        registro = [registro for registro in registros if registro['id'] == id]
        if len(registro) == 0:
            abort(404)
        print "SELECT"
        return {'registro': marshal(registro[0], registro_fields)}

    def put(self, id):
        registro = [registro for registro in registros if registro['id'] == id]
        if len(registro) == 0:
            abort(404)
        registro = registro[0]
        args = self.reqparse.parse_args()
        for k, v in args.items():
            if v is not None:
                registro[k] = v
                
        registro_obj = registro_dao.busca(id)
        registro_obj.nome = args['nome']
        registro_obj.valor = args['valor']
        registro_dao.mantem(registro_obj,False)
        print registro_dao.aviso
                
        print "EDITOU"
        return {'registro': marshal(registro, registro_fields)}

    def delete(self, id):
        registro = [registro for registro in registros if registro['id'] == id]
        if len(registro) == 0:
            abort(404)
            
        registro_obj = registro_dao.busca(id)
        registro_dao.mantem(registro_obj,True)
        print registro_dao.aviso
            
        registros.remove(registro[0])
        print "EXCLUIU"
        return {'result': True}

api.add_resource(RegistroListAPI, '/api/catraca/registros', endpoint='registros')
api.add_resource(RegistroAPI, '/api/catraca/registros/<int:id>', endpoint='registro')

#####################################################################
## FIM RECURSO REGISTRO
#####################################################################

if __name__ == '__main__':
    app.run(debug=True)
     
