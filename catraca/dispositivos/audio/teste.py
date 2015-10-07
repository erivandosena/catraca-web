import subprocess
import time
from time import sleep
from catraca.dispositivos.sensoroptico import SensorOptico
from catraca.pinos import PinoControle


rpi = PinoControle()
sensor_1 = rpi.ler(6)['gpio']
sensor_2 = rpi.ler(13)['gpio']


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
#     	while (codigo <> '01') or (codigo <> '00'):
#             beep('audio/beep-04.mp3')
#             time.sleep(1)
            
        
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

def registra_giro(tempo, operacao, codigo_giro):

    finaliza_giro = True
    try:
        # GIRO HORARIO
        if operacao == 1:
            print 'GIRO HORARIO'
            for segundo in range(tempo, -1, -1):
                tempo_decorrido = (tempo/1000)-(segundo/1000)
                print finaliza_giro
                print str(tempo_decorrido)+" de "+str(tempo/1000)
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
            print 'GIRO ANTIHORARIO'
            for segundo in range(tempo, -1, -1):
                tempo_decorrido = (tempo/1000)-(segundo/1000)
                #print finaliza_giro
                codigo_giro = str(ler_sensor(1)) + '' + str(ler_sensor(2))
                alerta_sonoro(10000,tempo_decorrido,tempo, codigo_giro)
                print str(tempo_decorrido)+" de "+str(tempo/1000)
                #if codigo_giro == '01':
                if tempo_decorrido == 17:
                    #codigo_giro = str(ler_sensor(2)) + '' + str(ler_sensor(1))
                    print 'Giro antihorario finalizado em '+ str(tempo_decorrido)+' segundo(s).'
                    finaliza_giro = False
                    return finaliza_giro
                #elif codigo_giro == '00':
                elif tempo_decorrido == 19:
                    #codigo_giro = str(ler_sensor(2)) + '' + str(ler_sensor(1))
                    print 'Giro antihorario finalizado em '+ str(tempo_decorrido)+' segundo(s).'
                    finaliza_giro = False
                    return finaliza_giro
            finaliza_giro = False
        return finaliza_giro
    except SystemExit, KeyboardInterrupt:
        raise
    except Exception, e:
        print 'Erro lendo sensores opticos: '+str(e)
    finally:
        pass
    
if registra_giro(20000, 2, '00'):
    print True
else:
    print False