#!/usr/bin/env python
# -*- coding: latin-1 -*-


import time
import locale
from time import sleep
from datetime import datetime


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production



class TesteHorarios(object):
    def __init__(self):
        super(TesteHorarios, self).__init__()

    def main(self):
        hora_atual = datetime.strptime(datetime.now().strftime('%H:%M:%S'),'%H:%M:%S').time()
        p1_hora_inicio = datetime.strptime('11:00:00','%H:%M:%S').time()
        p1_hora_fim = datetime.strptime('13:30:00','%H:%M:%S').time()
        p2_hora_inicio = datetime.strptime('17:30:00','%H:%M:%S').time()
        p2_hora_fim = datetime.strptime('19:00:00','%H:%M:%S').time()
    
#         if not (((hora_atual >= p1_hora_inicio) and (hora_atual <= p1_hora_fim)) or ((hora_atual >= p2_hora_inicio) and (hora_atual <= p2_hora_fim))):        
#             print 'self.aviso.exibir_horario_invalido()'
#             print 'self.aviso.exibir_acesso_bloqueado()'
#             print 'passou na validaoa de horarios'
#             return None
#         #elif (len(str(id_cartao)) <> 10):
#         el
        if False:    
            #self.log.logger.error('Cartao com ID incorreto:'+ str(id_cartao))
            print 'self.aviso.exibir_erro_leitura_cartao()'
            print 'self.aviso.exibir_aguarda_cartao()'
            return None
        #elif (len(str(id_cartao)) == 10):
        elif True:
            #cartao = self.busca_id_cartao(id_cartao)
            if False:
                #self.log.logger.info('Cartao nao cadastrado ID:'+ str(id_cartao))
                print 'self.aviso.exibir_cartao_nao_cadastrado()'
                print 'self.aviso.exibir_aguarda_cartao()'
                return None
            else:
                #creditos = cartao.creditos
                #usuario_cartao = cartao.tipo
                #tipo = self.tipo_usuario(usuario_cartao)
                
                hora_ultimo_acesso = datetime.strptime(datetime.now().strftime('%H:%M:%S'),'%H:%M:%S').time()
    
                datasis = datetime.now()
                data_atual = datetime(
                    day=datasis.day,
                    month=datasis.month,
                    year=datasis.year, 
                ).strptime(datasis.strftime('%d/%m/%Y'),'%d/%m/%Y')
                
                databd = datetime.now()
                data_ultimo_acesso = datetime(
                    day=databd.day,
                    month=databd.month,
                    year=databd.year, 
                ).strptime(databd.strftime('%d/%m/%Y'),'%d/%m/%Y')
    
                if ((hora_atual >= p1_hora_inicio) and (hora_atual <= p1_hora_fim)):
                    print 'passou na validação dia'
                    if ((hora_ultimo_acesso >= p1_hora_inicio) and (hora_ultimo_acesso <= p1_hora_fim) and (data_ultimo_acesso <= data_atual)):
                        print 'self.aviso.exibir_cartao_utilizado1()'
                        print 'self.aviso.exibir_acesso_bloqueado()'
                        print 'passou na validaoa de hora p/ 1ª refeicao dia'
                        return None    
                if ((hora_atual >= p2_hora_inicio) and (hora_atual <= p2_hora_fim)):
                    print 'passou na validação noite'
                    if ((hora_ultimo_acesso >= p2_hora_inicio) and (hora_ultimo_acesso <= p2_hora_fim) and (data_ultimo_acesso <= data_atual)):
                        print 'self.aviso.exibir_cartao_utilizado2()'
                        print 'self.aviso.exibir_acesso_bloqueado()'
                        print 'passou na validaoa de hora p/ 2ª refeicao noite'
                        return None
                #if (creditos == 0):
                if False:
                        #self.log.logger.info('Cartao sem credito ID:'+ str(id_cartao))
                        print 'self.aviso.exibir_cartao_sem_saldo(tipo)'
                        print 'self.aviso.exibir_acesso_bloqueado()'
                        return None
                else:  
                    print 'Finalizou...'
                    pass
                    