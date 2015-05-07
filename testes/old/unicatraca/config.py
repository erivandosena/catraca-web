#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

__author__ = "Erivando Sena"
__copyright__ = "Copyright 2015, Universidade da Integração Internacional da Lusofonia Afro-Brasileira"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


class Config:
    # Pinos raspberry Pi B Rev. 2
    PINOS = {
        3 : {'GPIO' : '2' , 'WiringPi' : '8', 'Pi4J' : '8', 'estado' : '0'},
        5 : {'GPIO' : '3' , 'WiringPi' : '9', 'Pi4J' : '9', 'estado' : '0'},
        7 : {'GPIO' : '4' , 'WiringPi' : '7', 'Pi4J' : '7', 'estado' : '0'},
        11 : {'GPIO' : '17' , 'WiringPi' : '0', 'Pi4J' : '0', 'estado' : '0'},
        12 : {'GPIO' : '18' , 'WiringPi' : '1', 'Pi4J' : '1', 'estado' : '0'},
        13 : {'GPIO' : '27' , 'WiringPi' : '2', 'Pi4J' : '2', 'estado' : '0'},
        15 : {'GPIO' : '22' , 'WiringPi' : '3', 'Pi4J' : '3', 'estado' : '0'},
        16 : {'GPIO' : '23' , 'WiringPi' : '4', 'Pi4J' : '4', 'estado' : '0'},
        18 : {'GPIO' : '24' , 'WiringPi' : '5', 'Pi4J' : '5', 'estado' : '0'},
        19 : {'GPIO' : '10' , 'WiringPi' : '12', 'Pi4J' : '12', 'estado' : '0'},
        21 : {'GPIO' : '9' , 'WiringPi' : '13', 'Pi4J' : '13', 'estado' : '0'},
        22 : {'GPIO' : '25' , 'WiringPi' : '6', 'Pi4J' : '6', 'estado' : '0'},
        23 : {'GPIO' : '11' , 'WiringPi' : '14', 'Pi4J' : '14', 'estado' : '0'},
        24 : {'GPIO' : '8' , 'WiringPi' : '10', 'Pi4J' : '10', 'estado' : '0'},
        26 : {'GPIO' : '7' , 'WiringPi' : '11', 'Pi4J' : '11', 'estado' : '0'}
    }
    DEBUG = True

