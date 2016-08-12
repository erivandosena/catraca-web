#!/usr/bin/env python
# -*- coding: latin-1 -*-


from catraca.logs import Logs
from catraca.modelo.dao.dao_generico import DAOGenerico
from catraca.modelo.entidades.catraca import Catraca


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class CatracaDAO(DAOGenerico):
    
    log = Logs()
    
    def __init__(self):
        super(CatracaDAO, self).__init__()
        DAOGenerico.__init__(self)
        
    def busca(self, *arg):
        arg = [a for a in arg][0] if arg else None
        if arg:
            sql = "SELECT "\
                "catr_id as id, "\
                "catr_interface_rede as interface, "\
                "catr_ip as ip, "\
                "catr_mac_lan as maclan, "\
                "catr_mac_wlan as macwlan, "\
                "catr_nome as nome, "\
                "catr_operacao as operacao, "\
                "catr_tempo_giro as tempo "\
                "FROM catraca WHERE "\
                "catr_id = %s"
        else:
            sql = "SELECT "\
                "catr_id as id, "\
                "catr_interface_rede as interface, "\
                "catr_ip as ip, "\
                "catr_mac_lan as maclan, "\
                "catr_mac_wlan as macwlan, "\
                "catr_nome as nome, "\
                "catr_operacao as operacao, "\
                "catr_tempo_giro as tempo "\
                "FROM catraca ORDER BY catr_id"
        return self.seleciona(Catraca, sql, arg)
    
    def busca_por_ip(self, ip):
        sql = "SELECT "\
            "catr_id as id, "\
            "catr_interface_rede as interface, "\
            "catr_ip as ip, "\
            "catr_mac_lan as maclan, "\
            "catr_mac_wlan as macwlan, "\
            "catr_nome as nome, "\
            "catr_operacao as operacao, "\
            "catr_tempo_giro as tempo "\
            "FROM catraca WHERE "\
            "catr_ip = %s"
        return self.seleciona(Catraca, sql, ip)
    
    def busca_por_nome(self, nome):
        sql = "SELECT "\
            "catr_id as id, "\
            "catr_interface_rede as interface, "\
            "catr_ip as ip, "\
            "catr_mac_lan as maclan, "\
            "catr_mac_wlan as macwlan, "\
            "catr_nome as nome, "\
            "catr_operacao as operacao, "\
            "catr_tempo_giro as tempo "\
            "FROM catraca WHERE "\
            "catr_nome = %s"
        print "LENDO TABELA CATRACA"
        return self.seleciona(Catraca, sql, nome.upper())
    
    def obtem_interface_rede(self, hostname):
        sql = "SELECT "\
            "catr_interface_rede as interface "\
            "FROM catraca WHERE "\
            "catr_nome = %s LIMIT 1"
        return self.seleciona(Catraca, sql, hostname.upper())
    
    def insere(self, obj):
        sql = "INSERT INTO catraca "\
            "("\
            "catr_id, "\
            "catr_interface_rede, "\
            "catr_ip, "\
            "catr_mac_lan, "\
            "catr_mac_wlan, "\
            "catr_nome, "\
            "catr_operacao, "\
            "catr_tempo_giro "\
            ") VALUES ("\
            "%s, %s, %s, %s, %s, %s, %s, %s)"
        return self.inclui(sql, obj)
    
    def atualiza(self, obj):
        sql = "UPDATE catraca SET "\
            "catr_interface_rede = %s, "\
            "catr_ip = %s, "\
            "catr_mac_lan = %s, "\
            "catr_mac_wlan = %s, "\
            "catr_nome = %s, "\
            "catr_operacao = %s, "\
            "catr_tempo_giro = %s "\
            "WHERE catr_id = %s"
        return self.altera(sql, obj)
    
    def exclui(self, *arg):
        obj = [a for a in arg][0] if arg else None
        sql = "DELETE FROM catraca"
        if obj:
            sql = str(sql) + " WHERE catr_id = %s"
        return self.deleta(sql, obj)
    
    def atualiza_exclui(self, obj, boleano):
        if obj or boleano:
            if boleano:
                if obj is None:
                    return self.exclui()
                else:
                    self.exclui(obj)
            else:
                return self.atualiza(obj)
            