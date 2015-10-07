#!/usr/bin/env python
# -*- coding: latin-1 -*-


import os
import socket
import locale
import datetime
from catraca.dao.registro import Registro
from catraca.dao.registrodao import RegistroDAO
from catraca.dao.cartaodao import CartaoDAO
from catraca.dao.catracadao import CatracaDAO
from catraca.dao.turnodao import TurnoDAO
from catraca.dao.finalidadedao import FinalidadeDAO
from time import sleep
from catraca.dispositivos.sensoroptico import SensorOptico
from catraca.pinos import PinoControle

import subprocess
import time
from time import sleep
from catraca.pinos import PinoControle


__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Unilab"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production



socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.connect(('unilab.edu.br', 0))
IP = '%s' % (socket.getsockname()[0])

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def main():
    print 'Iniciando os testes tabela registro...'
    
    registro = Registro()
    registro_dao = RegistroDAO()
    cartao_dao = CartaoDAO()
    turno_dao = TurnoDAO()
    catraca_dao = CatracaDAO()

    registro.data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    registro.giro = 1
    registro.valor = 0.01
    registro.cartao = cartao_dao.busca(1)
    registro.turno = turno_dao.busca(2)
    
    rpi = PinoControle()
    sensor_1 = rpi.ler(6)['gpio']
    sensor_2 = rpi.ler(13)['gpio']
    
#     if registro_dao.conexao_status():
#          print "conexao_status: "+ str(registro_dao.conexao_status())

# 
#     if not registro_dao.mantem(registro,False):
#         raise Exception(registro_dao.aviso)
#     else:
#         print registro_dao.aviso


#     print registro.cartao.perfil.tipo.nome
#     print registro.cartao.perfil.nome
#     print registro.cartao.numero
#     print locale.currency(registro.valor).format()

    #registro = registro_dao.busca(6)

    """
    registro_dao.mantem(registro,False)
    print registro_dao.aviso
    
    print registro.cartao


    catraca = CatracaDAO().busca_por_ip(IP)
    turnos = catraca.turno

    p1_hora_inicio = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()
    p1_hora_fim = datetime.datetime.strptime('00:00:00','%H:%M:%S').time()

    conta_turnos = 0
    hora_atual = datetime.datetime.strptime(datetime.datetime.now().strftime('%H:%M:%S'),'%H:%M:%S').time()
    for turno in turnos:
        conta_turnos += 1
        print conta_turnos
        p1_hora_inicio = datetime.datetime.strptime(str(turno[1]),'%H:%M:%S').time()
        p1_hora_fim = datetime.datetime.strptime(str(turno[2]),'%H:%M:%S').time()

        if ((hora_atual >= p1_hora_inicio) and (hora_atual <= p1_hora_fim)):
            finalidade_turno = FinalidadeDAO().busca(turno[3]).nome
            print "Turno encontrado entre:" +str(p1_hora_inicio)+" "+str(p1_hora_fim)+ " -> " + finalidade_turno
            break
    if not (((hora_atual >= p1_hora_inicio) and (hora_atual <= p1_hora_fim)) or ((hora_atual >= p1_hora_inicio) and (hora_atual <= p1_hora_fim))):
        print "Fora do horario!"
        return None
    elif ((hora_atual >= p1_hora_inicio) and (hora_atual <= p1_hora_fim)):
        print "Turno liberado entre:" +str(p1_hora_inicio)+" "+str(p1_hora_fim)
        print "faco coisas apartir daqui!"
    if True:
        print "outras coisas..."

            
    
    """  
#     
#     sensor_optico = SensorOptico()
#     
#     def aguarda_giro(tempo):
#         finaliza_tempo = True
#         contador = tempo/1000
#         while True:
#             if not sensor_optico.registra_giro(tempo):
#                 print "girou!"
#             else:
#                 print "nao girou"
# #             contador = contador -1
# #             print str(contador)
# #             #print str(self.tempo_decorrido)+" de "+str(tempo/1000)
# #             #self.tempo_decorrido = (tempo/1000)-(segundo/1000)
# #             #3decorrido = (contador/1000)-(tempo/1000)
# #             #print str(decorrido)
# #             if contador == 0:
# #                 print 'Finalizou no tempo decorrido de: '+ str(decorrido)
# #                 retfinaliza_tempo = False
#             
#             
#     aguarda_giro(30000)
    
    
#     print 62 * "="
#     print '======################### RELATORIO ####################======'
#     print 62 * "="
#     
#     
#     for registro in registro_dao.busca():
#         cartao = cartao_dao.busca(registro[4])
#         print str(registro[1]) +" "\
#         + str(registro[2]) +" "\
#         + str(registro[3]) +" "\
#         + str(cartao.numero) +" "\
#         + str(cartao.perfil.tipo.nome) +" "\
#         + str(TurnoDAO().busca(registro[5]))
#         print 62 * "-"
#     print 62 * "="

#     id = 3995148318
#         
#     def lista_cartoes():
# 
#         try:
#             lista = cartao_dao.busca()
#             lista.sort()
#             return lista
#         except SystemExit, KeyboardInterrupt:
#             raise
#         except Exception:
#             self.log.logger.error('Erro consultando ID.', exc_info=True)
#         finally:
#             pass
#         
#     cartoes = lista_cartoes()
#     
#     def pesquisa_id(lista, id):
#         resultado = None
#         for cartao in lista:
#             if cartao[1] == id:
#                 resultado = cartao
#                 return resultado
#                 break
#         return resultado
#       
#     cartao = pesquisa_id(cartoes, id)
#     if cartao is not None:
#         print cartao
#         print cartao[1]
#         print cartao[2]
#     else:
#         print 'não encontrado!'
#         
#     databd = cartao[3]
#     data_ultimo_acesso = datetime.datetime(
#         day=databd.day,
#         month=databd.month,
#         year=databd.year, 
#     ).strptime(databd.strftime('%d/%m/%Y'),'%d/%m/%Y')
#     
#     print data_ultimo_acesso.day
#     
#     def obtem_turno():
#         catraca = catraca_dao.busca_por_ip('10.5.2.253')
#         turnos = catraca.turnos
#         turnos.sort()
#         for turno in turnos:
#             hora_atual = datetime.datetime.strptime(datetime.datetime.now().strftime('%H:%M:%S'),'%H:%M:%S').time()
#             hora_inicio = datetime.datetime.strptime(str(turno[1]),'%H:%M:%S').time()
#             hora_fim = datetime.datetime.strptime(str(turno[2]),'%H:%M:%S').time()
#             if ((hora_atual >= hora_inicio) and (hora_atual <= hora_fim)):
#                 return turno
#                 break
#         return None
#         
#     print obtem_turno()
#     
#     print datetime.datetime.now()
#     print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     print datetime.datetime.strptime(datetime.datetime.now().strftime('%H:%M:%S'),'%H:%M:%S').time()
#     print datetime.datetime.now().strftime("%H:%M:%S")
#     
#     def teste(boleano):
#         status = False
#         try:
#             if boleano:            
#                 print 'testando...'
#                 status = True
#                 #/0
#             else:
#                 print 'nao testou!'
#         except SystemExit, KeyboardInterrupt:
#             raise
#         except Exception, e:
#             status = False
#             print 'Erro: '+ str(e) 
#         finally:
#             print 'teste finalizado!'   
#         return status
# 
#     print teste(True)
        
    
    def beep(mp3):
        process = subprocess.Popen(['mpg321 -q -g 100 '+mp3, '-R player'], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)#STDOUT
        stdout_value = process.communicate()[0]
        #print '\tstdout:', repr(stdout_value)
    
    
    # def alerta_sonoro(tempo,codigo): 
    #     contador = 0
    #     while contador < tempo:
    #         time.sleep(1)
    #         contador += 1
    #         print str(contador)
    #     else:
    #         while (codigo <> '01') or (codigo <> '00'):
    #             beep('audio/beep-04.mp3')
    #             time.sleep(1)
                
        
    def ler_sensor(sensor):
        if sensor == 1:
            return rpi.estado(sensor_1)
        elif sensor == 2:
            return rpi.estado(sensor_2)
            
    def alerta_sonoro(tempo, decorrido, tempo_giro, codigo_sensores):
        finaliza_giro = True
        if decorrido == 16:
            if decorrido < tempo_giro:
                for segundo in range(tempo, -1, -1):
                    if segundo/1000 == 10:
                        while codigo_sensores == '11':
                            beep('/home/pi/Catraca/catraca/dispositivos/audio/beep-04.mp3')
                            print 'bipando...'
                        else:
                            finaliza_giro = False
                            return finaliza_giro
            return finaliza_giro
        return finaliza_giro
                
    #if teste(60000):
    #    print True
    #else:
    #    print False
    #alerta_sonoro(10, '01')
        
    def registra_giro(tempo, operacao):
        codigo_giro = ''
        finaliza_giro = True
        try:
            # GIRO HORARIO
            if operacao == 1:
                print 'GIRO HORARIO'
                for segundo in range(tempo, -1, -1):
                    tempo_decorrido = (tempo/1000)-(segundo/1000)
                    print finaliza_giro
                    codigo_giro = str(ler_sensor(1)) + '' + str(ler_sensor(2))
                    print str(tempo_decorrido)+" de "+str(tempo/1000)
                    if ler_sensor(1) == 1 and ler_sensor(2) == 0:
                        codigo_giro = str(ler_sensor(1)) + '' + str(ler_sensor(2))
                        print 'Girou catraca no sentido horario, codigo sensores: '+ str(codigo_giro)
                        while ler_sensor(1) == 1 and ler_sensor(2) == 0:
                            codigo_giro = str(ler_sensor(1)) + '' + str(ler_sensor(2))
                            print 'Continuou o giro horario, codigo sensores: '+ str(codigo_giro)
                            codigo_giro = ''
                        while ler_sensor(1) == 1 and ler_sensor(2) == 1:
                            codigo_giro = str(self.ler_sensor(1)) + '' + str(self.ler_sensor(2))
                            print 'No meio do giro horario, codigo sensores: '+ str(codigo_giro)
                            #self.alerta_sonoro(10,codigo_giro)
                        while self.ler_sensor(1) == 0 and self.ler_sensor(2) == 1:
                            codigo_giro = str(self.ler_sensor(1)) + '' + str(self.ler_sensor(2))
                            self.log.logger.debug('Finalizando o giro horario, codigo sensores: '+ str(codigo_giro))
                    #if codigo_giro == '01': 
                    if tempo_decorrido == 11:
                        #codigo_giro = str(ler_sensor(1)) + '' + str(ler_sensor(2))
                        print 'Giro horario finalizado em '+ str(tempo_decorrido)+' segundo(s).'
                        finaliza_giro = False
                        return finaliza_giro
                    #elif codigo_giro == '00': 
                    elif tempo_decorrido == 13:
                        #codigo_giro = str(ler_sensor(1)) + '' + str(ler_sensor(2))
                        print 'Giro horario finalizado em '+ str(tempo_decorrido)+' segundo(s).'
                        finaliza_giro = False
                        return finaliza_giro
                finaliza_giro = False
            # GIRO ANTIHORARIO
            if operacao == 2:
                #print 'GIRO ANTIHORARIO'
                #for segundo in range(tempo, -1, -1):
                contador = 0
                while contador <= tempo/1000:
                    contador += 1
                    segundo = tempo/1000 - contador
                    #print str(contador)
                    #print str(tempo/1000)
                    #rint str(segundo)
                    #sleep(1)
                    #tempo_decorrido = (tempo/1000)-(segundo/1000)
                    tempo_decorrido = contador
                    #print finaliza_giro
                    #alerta_sonoro(10000,tempo_decorrido,tempo, codigo_giro)
                    #print str(tempo_decorrido)+"/"+str(tempo/1000)
                    #print str(segundo) + ' seg. restantes para expirar o tempo para giro.'
                    #print 'Catraca em repouso, codigo sensores: '+ str(ler_sensor(1)) + '' + str(ler_sensor(2))
                    if tempo_decorrido == tempo/1000:
                        finaliza_giro = False
                        return finaliza_giro
                    if ler_sensor(2) == 1 and ler_sensor(1) == 0:
                        codigo_giro = str(ler_sensor(2)) + '' + str(ler_sensor(1))
                        print 'Girou a catraca no sentido antihorario, codigo sensores: '+ str(codigo_giro)
                        while ler_sensor(2) == 1 and ler_sensor(1) == 0:
                            codigo_giro = str(ler_sensor(2)) + '' + str(ler_sensor(1))
                            print 'Continuou o giro antihorario, codigo sensores: '+ str(codigo_giro)
                            #self.alerta_sonoro(10,codigo_giro)
                            codigo_giro = ''
                        while ler_sensor(2) == 1 and ler_sensor(1) == 1:
                            codigo_giro = str(ler_sensor(2)) + '' + str(ler_sensor(1))
                            #self.alerta_sonoro(10,codigo_giro)
                            print 'No meio do giro antihorario, codigo sensores: '+ str(codigo_giro)
                        while ler_sensor(2) == 0 and ler_sensor(1) == 1:
                            codigo_giro = str(ler_sensor(2)) + '' + str(ler_sensor(1))
                            print 'Finalizando o giro antihorario, codigo sensores: '+ str(codigo_giro)
                            #self.alerta_sonoro(10,codigo_giro)
                    if codigo_giro == '01':
                    #if tempo_decorrido == 17:
                        codigo_giro = str(ler_sensor(2)) + '' + str(ler_sensor(1))
                        print 'Giro antihorario finalizado em '+ str(tempo_decorrido)+' segundo(s).'
                        finaliza_giro = False
                        return finaliza_giro
                    elif codigo_giro == '00':
                    #elif tempo_decorrido == 19:
                        #codigo_giro = str(ler_sensor(2)) + '' + str(ler_sensor(1))
                        print 'Giro antihorario finalizado em '+ str(tempo_decorrido)+' segundo(s).'
                        finaliza_giro = False
                        return finaliza_giro
                    sleep(1)
                else:
                    print 'finaliza_giro = False'
                    finaliza_giro = False
            print 'return finaliza_giro'
            return finaliza_giro
        except SystemExit, KeyboardInterrupt:
            raise
#         except Exception, e:
#             print 'Erro lendo sensores opticos: '+str(e)
        finally:
            pass
        
    def ler():
        while True:
            leitor()
            
    def leitor():
        #while True:
        print registra_giro(20000, 2)    
#         while registra_giro(20000, 2):
#             print 'GIROU!!!'
#             #return True
#             break
#         else:
#             print 'NAO GIROU!!!'
#             #return False
     
    ler()
        