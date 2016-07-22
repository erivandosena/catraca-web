#!/usr/bin/env python
# -*- coding: latin-1 -*-


from contextlib import closing
from catraca.logs import Logs
from catraca.modelo.dados.conexao import ConexaoFactory
from catraca.modelo.dados.conexaogenerica import ConexaoGenerica
from catraca.modelo.entidades.catraca import Catraca
from curses.ascii import NUL


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class CatracaDAO(ConexaoGenerica):
    
    log = Logs()
    
    def __init__(self):
        super(CatracaDAO, self).__init__()
        ConexaoGenerica.__init__(self)
 
    def busca(self, *arg):
        obj = Catraca()
        id = None
        for i in arg:
            id = i
        if id:
            sql = "SELECT catr_id, "\
                  "catr_ip, "\
                  "catr_tempo_giro, "\
                  "catr_operacao, "\
                  "catr_nome, "\
                  "catr_mac_lan, "\
                  "catr_mac_wlan, "\
                  "catr_interface_rede "\
                  "FROM catraca WHERE "\
                  "catr_id = " + str(id)
        elif id is None:
            sql = "SELECT catr_id, "\
                  "catr_ip, "\
                  "catr_tempo_giro, "\
                  "catr_operacao, "\
                  "catr_nome, "\
                  "catr_mac_lan, "\
                  "catr_mac_wlan, "\
                  "catr_interface_rede "\
                  "FROM catraca ORDER BY catr_id"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                if id:
                    dados = cursor.fetchone()
                    if dados is not None:
                        obj.id = dados[0]
                        obj.ip = dados[1]
                        obj.tempo = dados[2]
                        obj.operacao = dados[3]
                        obj.nome = dados[4]
                        obj.maclan = dados[5]
                        obj.macwlan = dados[6]
                        obj.interface = dados[7]
                        return obj
                    else:
                        return None
                elif id is None:
                    list = cursor.fetchall()
                    if list != []:
                        return list
                    else:
                        return None
        except Exception as excecao:
            self.aviso = str(excecao)
            self.log.logger.error('[catraca] Erro ao realizar SELECT.', exc_info=True)
        finally:
            pass
        
    def busca_por_ip(self, ip):
        obj = Catraca()
        sql = "SELECT catr_id, "\
              "catr_ip, "\
              "catr_tempo_giro, "\
              "catr_operacao, "\
              "catr_nome, "\
              "catr_mac_lan, "\
              "catr_mac_wlan, "\
              "catr_interface_rede "\
              "FROM catraca WHERE "\
              "catr_ip = '" + str(ip) + "'"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                dados = cursor.fetchone()
                if dados is not None:
                    obj.id = dados[0]
                    obj.ip = dados[1]
                    obj.tempo = dados[2]
                    obj.operacao = dados[3]
                    obj.nome = dados[4]
                    obj.maclan = dados[5]
                    obj.macwlan = dados[6]
                    obj.interface = dados[7]
                    print "LENDO TABELA CATRACA"
                    return obj
                else:
                    print "LENDO TABELA CATRACA VAZIA"
                    return None
        except Exception as excecao:
            self.aviso = str(excecao)
            self.log.logger.error('[catraca] Erro ao realizar SELECT.', exc_info=True)
        finally:
            pass
        
    def busca_por_nome(self, nome):
        obj = Catraca()
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                sql_select = 'SELECT catr_id, catr_ip, catr_tempo_giro, catr_operacao, catr_nome, ' +\
                'catr_mac_lan, catr_mac_wlan, catr_interface_rede FROM catraca WHERE catr_nome = %s'
                cursor.execute(sql_select % str("'" + nome.upper() + "'"))
                dados = cursor.fetchone()
                if dados is not None:
                    obj.id = dados[0]
                    obj.ip = dados[1]
                    obj.tempo = dados[2]
                    obj.operacao = dados[3]
                    obj.nome = dados[4]
                    obj.maclan = dados[5]
                    obj.macwlan = dados[6]
                    obj.interface = dados[7]
                    print "LENDO TABELA CATRACA"
                    return obj
                else:
                    print "LENDO TABELA CATRACA VAZIA"
                    return None
        except Exception as excecao:
            self.aviso = str(excecao)
            self.log.logger.error('[catraca] Erro ao realizar SELECT.', exc_info=True)
        finally:
            pass

    
    def obtem_interface_rede(self, hostname):
        obj = Catraca()
        sql = "SELECT catr_interface_rede FROM catraca WHERE catr_nome = '" + str(hostname).upper() + "' LIMIT 1"
        try:
            with closing(self.abre_conexao().cursor()) as cursor:
                cursor.execute(sql)
                dados = cursor.fetchone()
                if dados:
                    obj.interface = dados[0]
                    return str(obj.interface).lower()
        except Exception as excecao:
            self.aviso = str(excecao)
            self.log.logger.error('[catraca] Erro ao realizar SELECT.', exc_info=True)
        finally:
            pass
        
    def insere(self, obj):
        try:
            if obj:
                with closing(self.abre_conexao().cursor()) as cursor:
                    sql_insert = 'INSERT INTO catraca(' +\
                       'catr_id, ' +\
                       'catr_ip, ' +\
                       'catr_tempo_giro, ' +\
                       'catr_operacao, ' +\
                       'catr_nome, ' +\
                       'catr_mac_lan, ' +\
                       'catr_mac_wlan, ' +\
                       'catr_interface_rede) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
                    cursor.execute(sql_insert, (obj.id, 
                                                obj.ip,
                                                obj.tempo,
                                                obj.operacao,
                                                obj.nome,
                                                obj.maclan,
                                                obj.macwlan,
                                                obj.interface)
                                   )
                    self.commit()
                    self.aviso = "[catraca] Inserido com sucesso!"
                    return True
            else:
                self.aviso = "[catraca] inexistente!"
                return False
        except Exception as excecao:
            self.aviso = str(excecao)
            self.log.logger.error('[catraca] Erro realizando INSERT.', exc_info=True)
            return False
        finally:
            pass   
        
    def atualiza_exclui(self, obj, delete):
        try:
            if obj or delete:
                with closing(self.abre_conexao().cursor()) as cursor:
                    if delete:
                        if obj is None:
                            sql_delete = 'DELETE FROM catraca'
                            cursor.execute(sql_delete)
                        else:
                            sql_delete = sql_delete +' WHERE catr_id = %s'
                            cursor.execute(sql_delete, (obj.id))
                        self.commit()
                        self.aviso = "[catraca] Excluido com sucesso!"
                        return True
                    else:
                        sql_update = 'UPDATE catraca SET catr_ip = %s, ' +\
                              'catr_tempo_giro = %s, ' +\
                              'catr_operacao = %s, ' +\
                              'catr_nome = %s, ' +\
                              'catr_mac_lan = %s, ' +\
                              'catr_mac_wlan = %s, ' +\
                              'catr_interface_rede = %s ' +\
                              'WHERE catr_id = %s'
                        cursor.execute(sql_update, (obj.ip, 
                                                    obj.tempo,
                                                    obj.operacao,
                                                    obj.nome,
                                                    obj.maclan,
                                                    obj.macwlan,
                                                    obj.interface,
                                                    obj.id)
                                       )
                        self.commit()
                        self.aviso = "[catraca] Alterado com sucesso!"
                        return True
            else:
                self.aviso = "[catraca] inexistente!"
                return False
        except Exception as excecao:
            self.aviso = str(excecao)
            self.log.logger.error('[catraca] Erro realizando UPDATE/DELETE.', exc_info=True)
            return False
        finally:
            pass
        