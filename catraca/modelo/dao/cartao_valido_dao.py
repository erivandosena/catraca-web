#!/usr/bin/env python
# -*- coding: latin-1 -*-


from catraca.logs import Logs
from catraca.modelo.dao.dao_generico import DAOGenerico
from catraca.modelo.entidades.cartao_valido import CartaoValido


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


class CartaoValidoDAO(DAOGenerico):
    
    log = Logs()

    def __init__(self):
        super(CartaoValidoDAO, self).__init__()
        DAOGenerico.__init__(self)
        
    def busca_cartao_valido(self, numero):
        sql = "SELECT "\
            "vinculo.vinc_avulso as avulso, "\
            "cartao.cart_creditos as creditos, "\
            "vinculo.vinc_descricao as descricao, "\
            "vinculo.vinc_fim as fim, "\
            "cartao.cart_id as id, "\
            "usuario.id_base_externa as idexterno, "\
            "vinculo.vinc_inicio as inicio, "\
            "SUBSTR(TRIM(usuario.usua_nome), 0, 16) || '.' as nome, "\
            "tipo.tipo_nome as nometipo, "\
            "cartao.cart_numero as numero, "\
            "vinculo.vinc_refeicoes as refeicoes, "\
            "tipo.tipo_id as tipo, "\
            "tipo.tipo_valor as valor, "\
            "vinculo.vinc_id as vinculo "\
            "FROM cartao "\
            "INNER JOIN tipo ON cartao.tipo_id = tipo.tipo_id "\
            "INNER JOIN vinculo ON vinculo.cart_id = cartao.cart_id "\
            "INNER JOIN usuario ON usuario.usua_id = vinculo.usua_id "\
            "WHERE cartao.cart_numero = %s"
        try:
            return self.seleciona(CartaoValido, sql, numero)
        finally:
            pass
            