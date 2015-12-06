#!/usr/bin/env python
# -*- coding: utf-8 -*-


from time import sleep
import subprocess
import threading
from multiprocessing import Process
from threading import Thread
from catraca.logs import Logs
from catraca.util import Util
from catraca.visao.interface.aviso import Aviso
from catraca.controle.raspberrypi.pinos import PinoControle
from catraca.controle.dispositivos.solenoide import Solenoide


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype"  # Prototype | Development | Production 


class SensorOptico(object):

    log = Logs()
    util = Util()
    aviso = Aviso()
    rpi = PinoControle()
    sensor_1 = rpi.ler(6)['gpio']
    sensor_2 = rpi.ler(13)['gpio']
    solenoide = Solenoide()
    tempo_decorrido = 0
    tempo_decorrente = 0
    finaliza_giro = False
    status_alerta = False
    

    def __init__(self):
        super(SensorOptico, self).__init__()

    def ler_sensor(self, sensor):
        if sensor == 1:
            return self.rpi.estado(self.sensor_1)
        elif sensor == 2:
            return self.rpi.estado(self.sensor_2)
        
    def registra_giro(self, tempo, catraca):
        tempo = tempo*1000;
        confirma_giro_completo = ''
        codigo_giro_completo = ''
        giro = None
        try:
            ##############################################################
            ## INICIA CRONOMETRO REGRESSIVO PARA O GIRO EM MILISSEGUNDOS
            ##############################################################
            while self.tempo_decorrente < tempo:
                self.cronometro_tempo(self.tempo_decorrido, tempo, 1.6)
                self.tempo_decorrido =  self.tempo_decorrente /1000
                self.log.logger.debug(str(self.tempo_decorrido) + ' seg. restantes para expirar o tempo de giro.')
                ##############################################################
                ## CATRACA SEM MOVIMENTO DE GIROS HORARIO OU ANTIHORARIO
                ##############################################################
                if self.obtem_codigo_sensores() == '00':
                    self.log.logger.debug('Catraca em repouso, codigo sensores: '+ self.obtem_codigo_sensores())
                ##############################################################
                ## INICIANDO VERIFICA SE HOUVE ALGUM GIRO HORARIO OU ANTIHORARIO
                ##############################################################
                if self.obtem_codigo_sensores() == '10' or self.obtem_codigo_sensores() == '01' or self.obtem_codigo_sensores() == '11':
                    ##############################################################
                    ## CAPTURA O TIPO DE GIRO EXECUTADO
                    ##############################################################
                    if giro is None:
                        giro = self.obtem_direcao_giro()
                    ##############################################################
                    ## VERIFICA SE O GIRO EXECUTADO CONVEM COM O HABILIRADO
                    ##############################################################
                    if self.obtem_giro_iniciado(giro) == catraca.operacao:
                        self.log.logger.info('Girou a catraca no sentido '+giro)
                        ##############################################################
                        ## VERIFICA SE O GIRO FOI HORARIO OU ANTIHORARIO
                        ##############################################################
                        while self.obtem_codigo_sensores() == '10' or self.obtem_codigo_sensores() == '01':
                            self.log.logger.debug('Continuou o giro '+giro+', codigo sensores: '+ self.obtem_codigo_sensores())
                            self.cronometro_tempo(self.tempo_decorrido, tempo, 1.6)
                        #cronometro_beep = 0
                        ##############################################################
                        ## VERIFICA SE A CATRACA SE ENCONTRA EM MEIO GIRO
                        ##############################################################
                        self.util.cronometro = 0
                        while self.obtem_codigo_sensores() == '11':
                            confirma_giro_completo = self.obtem_codigo_sensores()
                            self.log.logger.debug('No meio do giro '+giro+', codigo sensores: '+ self.obtem_codigo_sensores())
                            ##############################################################
                            ## ALERTA CASO A CATRACA PARE NO MEIO DO GIRO MAIS DE 10 SEG
                            ##############################################################
                            if self.status_alerta:
                                self.status_alerta = False

                            if self.util.cronometro == 0:
                                self.aviso.exibir_uso_incorreto()
                                self.status_alerta = True
                                self.aviso.exibir_acesso_liberado()
                                
                            self.util.beep_buzzer_delay(860, 1, 1, 10) #10 = 10 seg
                            if self.util.cronometro/1000 == 10:
                                self.util.cronometro = 0

                        codigo_giro_completo = self.obtem_codigo_sensores()
                        ##############################################################
                        ## FINALIZANDO VERIFICA SE O GIRO FOI HORARIO OU ANTIHORARIO
                        ##############################################################
                        while self.obtem_codigo_sensores() == '10' or self.obtem_codigo_sensores() == '01':
                            self.log.logger.debug('Finalizando o giro '+giro+', codigo sensores: '+ self.obtem_codigo_sensores())
                        codigo_giro_completo += self.obtem_codigo_sensores()
                        confirma_giro_completo += codigo_giro_completo
                        print codigo_giro_completo
                        ##############################################################
                        ## VERIFICA SE O GIRO FOI COMPLETADO CORRETAMENTE OU NAO
                        ##############################################################
                        if giro == 'antihorario':
                            if confirma_giro_completo == '111000' or confirma_giro_completo == '110000':
                                self.log.logger.info('Giro '+giro+' finalizado em '+ str(self.tempo_decorrido)+' segundo(s) no codigo: '+ self.obtem_codigo_sensores())
                                self.finaliza_giro = True
                                return self.finaliza_giro
                            else:
                                self.finaliza_giro = False
                                self.cronometro_tempo(self.tempo_decorrido, tempo, 1.6)
                        if giro == 'horario':
                            if confirma_giro_completo == '110100' or confirma_giro_completo == '110000' and self.cronometro_tempo(self.tempo_decorrido, tempo, 1.6) == True:
                                self.log.logger.info('Giro '+giro+' finalizado em '+ str(self.tempo_decorrido)+' segundo(s) no codigo: '+ self.obtem_codigo_sensores())
                                self.finaliza_giro = True
                                return self.finaliza_giro
                            else:
                                self.finaliza_giro = False
                                self.cronometro_tempo(self.tempo_decorrido, tempo, 1.6)
                    ##############################################################
                    ## FINALIZA GIRO INCORRETO
                    ##############################################################
                    else:
                        self.log.logger.info('Nao girou '+giro+ ', operacao cancelada.')
                        self.finaliza_giro = False
                        self.tempo_decorrente = tempo/1000
                        return self.finaliza_giro
            self.cronometro_tempo(self.tempo_decorrido, tempo, 1.6)
            self.tempo_decorrente = 0
        except SystemExit, KeyboardInterrupt:
            raise
        except Exception:
            self.log.logger.error('Erro lendo sensores opticos.', exc_info=True)
        finally:
            self.tempo_decorrente = 0
            confirma_giro_completo = ''
            codigo_giro_completo = ''
            giro = None
            return self.finaliza_giro

    def obtem_codigo_sensores(self):
        return str(self.ler_sensor(1)) + '' + str(self.ler_sensor(2))
    
    def obtem_direcao_giro(self):
        opcoes = {
                   '10' : 'horario',
                   '01' : 'antihorario',
                   '11' : 'incompleto',
                   '00' : 'repouso',
        }
        return opcoes.get(self.obtem_codigo_sensores(), None)
    
    def obtem_giro_iniciado(self, modo_operacao):
        opcoes = {
                   'horario' : 1,
                   'antihorario' : 2,
        }
        return opcoes.get(modo_operacao, None)
   
    def cronometro_tempo(self, tempo_decorrido, tempo, milissegundos):
        self.tempo_decorrente += milissegundos
        if tempo_decorrido > tempo/1000:
            self.log.logger.info('Tempo expirado em '+ str(tempo_decorrido)+' segundo(s) sem giro.')
            self.finaliza_giro = False
            return self.finaliza_giro
        else:
            return True
        
        