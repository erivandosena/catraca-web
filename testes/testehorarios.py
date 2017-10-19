#!/usr/bin/env python
# -*- coding: latin-1 -*-


import time
import locale
from time import sleep
#from datetime import datetime
import datetime
import calendar


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"



class TesteHorarios(object):
    
    def __init__(self):
        super(TesteHorarios, self).__init__()

    def horarios(self):
        hora_atual = datetime.datetime.strptime(datetime.datetime.now().strftime('%H:%M:%S'),'%H:%M:%S').time()
        p1_hora_inicio = datetime.datetime.strptime('11:00:00','%H:%M:%S').time()
        p1_hora_fim = datetime.datetime.strptime('13:30:00','%H:%M:%S').time()
        p2_hora_inicio = datetime.datetime.strptime('17:30:00','%H:%M:%S').time()
        p2_hora_fim = datetime.datetime.strptime('19:00:00','%H:%M:%S').time()
    
        if not self.dias_uteis():
            print 'self.aviso.exibir_dia_invalido'
            print 'self.aviso.exibir_acesso_bloqueado()'
            print 'passou na validacao de dias uteis'
            return None
        if not (((hora_atual >= p1_hora_inicio) and (hora_atual <= p1_hora_fim)) or ((hora_atual >= p2_hora_inicio) and (hora_atual <= p2_hora_fim))):        
            print 'self.aviso.exibir_horario_invalido()'
            print 'self.aviso.exibir_acesso_bloqueado()'
            print 'passou na validaoa de horarios'
            return None
        #elif (len(str(id_cartao)) <> 10):
        elif False:    
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
                
                hora_ultimo_acesso = datetime.datetime.strptime(datetime.datetime.now().strftime('%H:%M:%S'),'%H:%M:%S').time()
    
                datasis = datetime.datetime.now()
                data_atual = datetime.datetime(
                    day=datasis.day,
                    month=datasis.month,
                    year=datasis.year, 
                ).strptime(datasis.strftime('%d/%m/%Y'),'%d/%m/%Y')
                
                databd = datetime.datetime.now()
                data_ultimo_acesso = datetime.datetime(
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

    def getPreviousBusinessDay(self, fromDate):
            previousBuinessDate = datetime.datetime.strptime(fromDate, "%d/%m/%Y")
            previousBuinessDate = previousBuinessDate + datetime.timedelta(days=-1)
            if datetime.date.weekday(previousBuinessDate) not in range(0,5):
                    previousBuinessDate = previousBuinessDate + datetime.timedelta(days=-1)
            if datetime.date.weekday(previousBuinessDate) not in range(0,5):
                    previousBuinessDate = previousBuinessDate + datetime.timedelta(days=-1)
            return previousBuinessDate.strftime('%d/%m/%Y')

    def dias_uteis(self):
        dia_util = True
        weekday_count = 0
        cal = calendar.Calendar()
        data_atual = datetime.datetime.now()
        for week in cal.monthdayscalendar(data_atual.year, data_atual.month):
            for i, day in enumerate(week):
                if (day == 0) or (i >= 5):
                    if (day <> 0) and (day <> data_atual.day):
                        print str(day) + ' não é dia útil'
                    if day == data_atual.day:
                        dia_util = False
                        print str(day) + ' não é dia útil [HOJE]'
                    continue
                if day == data_atual.day:
                    dia_util = True
                    print str(day) + ' é dia útil [HOJE]'
                else:
                    print str(day) + ' é dia útil'
                
                weekday_count += 1
        print 'Total de dias uteis: '+str(weekday_count)
        return dia_util


    def main(self):
        #self.horarios()
        testDate = datetime.datetime.now()
        
       # print self.getPreviousBusinessDay(testDate)
        #print self.dias_uteis()
        self.horarios()
        
#         for x in range(1,100) :
#             testDate=self.getPreviousBusinessDay(testDate)
#             print testDate
        
        
                    