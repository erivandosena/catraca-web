#!/usr/bin/env python
# -*- coding: latin-1 -*-


import socket
import locale
from time import sleep
from catraca.logs import Logs
from catraca.pinos import PinoControle
from catraca.dispositivos.solenoide import Solenoide

from catraca.dao.catracadao import CatracaDAO


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


log = Logs()
rpi = PinoControle()
sensor_1 = rpi.ler(6)['gpio']
sensor_2 = rpi.ler(13)['gpio']

def ler_sensor(sensor):
    if sensor == 1:
        return rpi.estado(sensor_1)
    elif sensor == 2:
        return rpi.estado(sensor_2)

def registra_giro(tempo):
    codigo_giro = ''
    tempo_giro = tempo
    catraca = CatracaDAO().busca_por_ip(obtem_ip())
    # cronômetro regressivo para o giro
    try:
        for segundo in range(tempo, -1, -1):
            tempo_giro -= segundo
            log.logger.debug(str(segundo / 1000) + ' seg. restantes para expirar o tempo para giro.')
            log.logger.debug('Catraca em repouso, codigo sensores: '+ str(ler_sensor(1)) + '' + str(ler_sensor(2)))
            print 'Catraca em repouso, codigo sensores: '+ str(ler_sensor(1)) + '' + str(ler_sensor(2))
            # GIRO HORARIO
            if catraca.operacao == 1:
                if ler_sensor(1) == 1 and ler_sensor(2) == 0:
                    log.logger.info('Girou catraca no sentido horario.')
                    print 'Girou catraca no sentido horario.'
                    while ler_sensor(1) == 1 and ler_sensor(2) == 0:
                        codigo_giro = str(ler_sensor(1)) + '' + str(ler_sensor(2))
                        log.logger.debug('Continuou o giro horario, codigo sensores: '+ str(codigo_giro))
                        print 'Continuou o giro horario, codigo sensores: '+ str(codigo_giro)
                        codigo_giro = ''
                    while ler_sensor(1) == 1 and ler_sensor(2) == 1:
                        codigo_giro = str(ler_sensor(1)) + '' + str(ler_sensor(2))
                        log.logger.debug('No meio do giro horario, codigo sensores: '+ str(codigo_giro))
                        print 'No meio do giro horario, codigo sensores: '+ str(codigo_giro)
                    while ler_sensor(1) == 0 and ler_sensor(2) == 1:
                        codigo_giro = str(ler_sensor(1)) + '' + str(ler_sensor(2))
                        log.logger.debug('Finalizando o giro horario, codigo sensores: '+ str(codigo_giro))
                        print 'Finalizando o giro horario, codigo sensores: '+ str(codigo_giro)
                    if codigo_giro == '01': 
                        codigo_giro = str(ler_sensor(1)) + '' + str(ler_sensor(2))
                        log.logger.info('Giro horario finalizado em '+ str(segundo/1000)+' segundo(s).')
                        print 'Giro horario finalizado em '+ str(segundo/1000)+' segundo(s).'
                        log.logger.debug('Giro horario completo no codigo: '+ str(codigo_giro))
                        print 'Giro horario completo no codigo: '+ str(codigo_giro)
                        return True
                    elif codigo_giro == '00': 
                        codigo_giro = str(ler_sensor(1)) + '' + str(ler_sensor(2))
                        log.logger.info('Giro horario finalizado em '+ str(segundo/1000)+' segundo(s).')
                        print 'Giro horario finalizado em '+ str(segundo/1000)+' segundo(s).'
                        log.logger.debug('Giro horario completo no codigo: '+ str(codigo_giro))
                        print 'Giro horario completo no codigo: '+ str(codigo_giro)
                        return True
            if catraca.operacao == 2:
                # GIRO ANTIHORARIO
                if ler_sensor(2) == 1 and ler_sensor(1) == 0:
                    log.logger.info('Girou a catraca no sentido antihorario.')
                    print 'Girou a catraca no sentido antihorario.'
                    while ler_sensor(2) == 1 and ler_sensor(1) == 0:
                        codigo_giro = str(ler_sensor(2)) + '' + str(ler_sensor(1))
                        log.logger.debug('Continuou o giro antihorario, codigo sensores: '+ str(codigo_giro))
                        print 'Continuou o giro antihorario, codigo sensores: '+ str(codigo_giro)
                        codigo_giro = ''
                    while ler_sensor(2) == 1 and ler_sensor(1) == 1:
                        codigo_giro = str(ler_sensor(2)) + '' + str(ler_sensor(1))
                        log.logger.debug('No meio do giro antihorario, codigo sensores: '+ str(codigo_giro))
                        print 'No meio do giro antihorario, codigo sensores: '+ str(codigo_giro)
                    while ler_sensor(2) == 0 and ler_sensor(1) == 1:
                        codigo_giro = str(ler_sensor(2)) + '' + str(ler_sensor(1))
                        log.logger.debug('Finalizando o giro antihorario, codigo sensores: '+ str(codigo_giro))
                        print 'Finalizando o giro antihorario, codigo sensores: '+ str(codigo_giro)
                    if codigo_giro == '01':
                        codigo_giro = str(ler_sensor(2)) + '' + str(ler_sensor(1))
                        log.logger.info('Giro antihorario finalizado em '+ str(tempo_giro/1000)+' segundo(s).')
                        print 'Giro antihorario finalizado em '+ str(tempo_giro/1000)+' segundo(s).'
                        log.logger.debug('Giro antihorario completo no codigo: '+ str(codigo_giro))
                        print 'Giro antihorario completo no codigo: '+ str(codigo_giro)
                        print str(tempo_giro)
                        return True
                    elif codigo_giro == '00': 
                        codigo_giro = str(ler_sensor(2)) + '' + str(ler_sensor(1))
                        log.logger.info('Giro antihorario finalizado em '+ str(tempo_giro/1000)+' segundo(s).')
                        print 'Giro antihorario finalizado em '+ str(tempo_giro/1000)+' segundo(s).'
                        log.logger.debug('Giro antihorario completo no codigo: '+ str(codigo_giro))
                        print 'Giro antihorario completo no codigo: '+ str(codigo_giro)
                        print str(tempo_giro)
                        return True
        return False
    except SystemExit, KeyboardInterrupt:
        raise
    except Exception:
        log.logger.error('Erro lendo sensores opticos.', exc_info=True)
    finally:
        pass

def obtem_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('unilab.edu.br', 0))
    ip = '%s' % ( s.getsockname()[0] )
    return ip

def direciona_giro():
    #1 = Giros Horario/Anti-horario(Entrada controlada com saida bloqueada)
    #2 = Giros Horario/Anti-horario(Saida liberada com entrada bloqueada)
    #3 = Giros Horario/Anti-horario(Entrada e saida liberadas)
    catraca = CatracaDAO().busca_por_ip(obtem_ip())
    solenoide = Solenoide()
    if catraca.operacao == 1:
        if ler_sensor(1) == 1 and ler_sensor(2) == 0:
#             solenoide.ativa_solenoide(1,1)
#             solenoide.ativa_solenoide(2,0)
#         else:
#             solenoide.ativa_solenoide(1,0)
            return 1
            
    elif catraca.operacao == 2:
        if ler_sensor(2) == 1 and ler_sensor(1) == 0:
#             solenoide.ativa_solenoide(2,1)
#             solenoide.ativa_solenoide(1,0)
#         else:
#             solenoide.ativa_solenoide(2,0)
            return 2
    
    elif catraca.operacao == 3:
        if (ler_sensor(1) == 1 and ler_sensor(2) == 0) or (ler_sensor(2) == 1 and ler_sensor(1) == 0):
#             solenoide.ativa_solenoide(1,1)
#             solenoide.ativa_solenoide(2,1)
#         else:
#             solenoide.ativa_solenoide(1,0)
#             solenoide.ativa_solenoide(2,0)
            return 3
        

def main():
    print 'Iniciando os testes controlegiro...'
    #while True:
    registra_giro(100000)
    #direciona_giro()
    