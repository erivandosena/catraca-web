#!/usr/bin/env python
# -*- coding: latin-1 -*-


from contextlib import closing
from catraca.modelo.dados.conexao import ConexaoFactory
from catraca.modelo.dados.conexaogenerica import ConexaoGenerica
from catraca.modelo.entidades.mensagem import Mensagem
from catraca.modelo.dao.catraca_dao import CatracaDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class MensagemDAO(ConexaoGenerica):

    def __init__(self):
        super(MensagemDAO, self).__init__()
        ConexaoGenerica.__init__(self)

    def busca(self, *arg):
        obj = Mensagem()
        id = None
        for i in arg:
            id = i
        if id:
            sql = "SELECT mens_id, mens_inicializacao, mens_saldacao, mens_aguardacartao, "\
            "mens_erroleitor, mens_bloqueioacesso, mens_liberaacesso, mens_semcredito, "\
            "mens_semcadastro, mens_cartaoinvalido, mens_turnoinvalido, mens_datainvalida, "\
            "mens_cartaoutilizado, mens_institucional1, mens_institucional2, "\
            "mens_institucional3, mens_institucional4, catr_id FROM mensagem WHERE mens_id = " + str(id)
        elif id is None:
            sql = "SELECT mens_id, mens_inicializacao, mens_saldacao, mens_aguardacartao, "\
            "mens_erroleitor, mens_bloqueioacesso, mens_liberaacesso, mens_semcredito, "\
            "mens_semcadastro, mens_cartaoinvalido, mens_turnoinvalido, mens_datainvalida, "\
            "mens_cartaoutilizado, mens_institucional1, mens_institucional2, "\
            "mens_institucional3, mens_institucional4, catr_id FROM mensagem ORDER BY mens_id"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        obj.id = dados[0]
                        obj.msg_inicializacao = dados[1]
                        obj.msg_saldacao = dados[2]
                        obj.msg_aguardacartao = dados[3]
                        obj.msg_erroleitor = dados[4]
                        obj.msg_bloqueioacesso = dados[5]
                        obj.msg_liberaacesso = dados[6]
                        obj.msg_semcredito = dados[7]
                        obj.msg_semcadastro = dados[8]
                        obj.msg_cartaoinvalido = dados[9]
                        obj.msg_turnoinvalido = dados[10]
                        obj.msg_datainvalida = dados[11]
                        obj.msg_cartaoutilizado = dados[12]
                        obj.msg_institucional1 = dados[13]
                        obj.msg_institucional2 = dados[14]
                        obj.msg_institucional3 = dados[15]
                        obj.msg_institucional4 = dados[16]
                        obj.catraca = self.busca_por_catraca(obj)
                        return obj
                    else:
                        return None
                elif id is None:
                    list = cursor.fetchall()
                    if list != []:
                        return list
                    else:
                        return None
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro ao realizar SELECT na tabela mensagem.', exc_info=True)
        finally:
            pass
        
    def busca_por_catraca(self, obj):
        return CatracaDAO().busca(obj.id)
    
    def insere(self, obj):
        try:
            if obj:
                sql = "INSERT INTO mensagem("\
                    "mens_id, "\
                    "mens_inicializacao, "\
                    "mens_saldacao, "\
                    "mens_aguardacartao, "\
                    "mens_erroleitor, "\
                    "mens_bloqueioacesso, "\
                    "mens_liberaacesso, "\
                    "mens_semcredito, "\
                    "mens_semcadastro, "\
                    "mens_cartaoinvalido, "\
                    "mens_turnoinvalido, "\
                    "mens_datainvalida, "\
                    "mens_cartaoutilizado, "\
                    "mens_institucional1, "\
                    "mens_institucional2, "\
                    "mens_institucional3, "\
                    "mens_institucional4, "\
                    "catr_id) VALUES (" +\
                    str(obj.id) + ", '" +\
                    str(obj.msg_inicializacao) + "', '" +\
                    str(obj.msg_saldacao) + "', '" +\
                    str(obj.msg_aguardacartao) + "', '" +\
                    str(obj.msg_erroleitor) + "', '" +\
                    str(obj.msg_bloqueioacesso) + "', '" +\
                    str(obj.msg_liberaacesso) + "', '" +\
                    str(obj.msg_semcredito) + "', '" +\
                    str(obj.msg_semcadastro) + "', '" +\
                    str(obj.msg_cartaoinvalido) + "', '" +\
                    str(obj.msg_turnoinvalido) + "', '" +\
                    str(obj.msg_datainvalida) + "', '" +\
                    str(obj.msg_cartaoutilizado) + "', '" +\
                    str(obj.msg_institucional1) + "', '" +\
                    str(obj.msg_institucional2) + "', '" +\
                    str(obj.msg_institucional3) + "', '" +\
                    str(obj.msg_institucional4) + "', " +\
                    str(obj.catraca.id) + ")"
                self.aviso = "Inserido com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    return True
            else:
                self.aviso = "Objeto inexistente!"
                return False
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro realizando INSERT na tabela mensagem.', exc_info=True)
            return False
        finally:
            pass

    def atualiza_exclui(self, obj, delete):
        try:
            if obj:
                if delete:
                    if obj.id:
                        sql = "DELETE FROM mensagem WHERE mens_id = " + str(obj.id)
                    else:
                        sql = "DELETE FROM mensagem"
                    msg = "Excluido com sucesso!"
                else:
                    self.aviso = "UPDATE mensagem SET " +\
                        "mens_inicializacao = '" + str(obj.msg_inicializacao) + "', " +\
                        "mens_saldacao = '" + str(obj.msg_saldacao) + "', " +\
                        "mens_aguardacartao = '" + str(obj.msg_aguardacartao) + "', " +\
                        "mens_erroleitor = '" + str(obj.msg_erroleitor) + "', " +\
                        "mens_bloqueioacesso = '" + str(obj.msg_bloqueioacesso) + "', " +\
                        "mens_liberaacesso = '" + str(obj.msg_liberaacesso) + "', " +\
                        "mens_semcredito = '" + str(obj.msg_semcredito) + "', " +\
                        "mens_semcadastro = '" + str(obj.msg_semcadastro) + "', " +\
                        "mens_cartaoinvalido = '" + str(obj.msg_cartaoinvalido) + "', " +\
                        "mens_turnoinvalido = '" + str(obj.msg_turnoinvalido) + "', " +\
                        "mens_datainvalida = '" + str(obj.msg_datainvalida) + "', " +\
                        "mens_cartaoutilizado = '" + str(obj.msg_cartaoutilizado) + "', " +\
                        "mens_institucional1 = '" + str(obj.msg_institucional1) + "', " +\
                        "mens_institucional2 = '" + str(obj.msg_institucional2) + "', " +\
                        "mens_institucional3 = '" + str(obj.msg_institucional3) + "', " +\
                        "mens_institucional4 = '" + sstr(obj.msg_institucional4) + "', " +\
                        "catr_id = " + str(obj.catraca.id) +\
                        " WHERE "\
                        "mens_id = " + str(obj.id)
                    self.aviso = "Alterado com sucesso!"
                with closing(self.abre_conexao().cursor()) as cursor:
                    cursor.execute(sql)
                    self.commit()
                    return True
            else:
                self.aviso = "Objeto inexistente!"
                return False
        except Exception, e:
            self.aviso = str(e)
            self.log.logger.error('Erro realizando DELETE/UPDATE na tabela mensagem.', exc_info=True)
            return False
        finally:
            pass
        