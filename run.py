#!/usr/bin/env python
# -*- coding: utf-8 -*-


from catraca.logs import Logs
from catraca.visao.interface.inicializador import Inicializador


__author__ = "Erivando Sena" 
__copyright__ = "(C) Copyright 2015, Unilab - Universidade da Integracao Internacional da Lusofonia Afro-Brasileira" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


if __name__ == '__main__':
    print "\nIniciando..."
    print ''
    print '|||||| |||||| ||'
    print '||  || ||  ||   '
    print '|||||| |||||| ||'
    print '||  || ||     ||'
    print '||  || ||     ||  v. Beta'
    print ''
    print '  ||||||||||   |||||||   |||||||||||   |||||||     |||||||     ||||||||||   |||||||'  
    print ' ||||||||||   |||||||||  |||||||||||  |||||||||   |||||||||   ||||||||||   ||||||||| '
    print '||||         ||||   ||||    |||||    ||||   |||| ||||   |||| ||||         ||||   ||||'
    print '|||          |||     |||     |||     |||     ||| |||     ||| |||          |||     |||'
    print '|||          |||     |||     |||     |||     ||| |||     ||| |||          |||     |||'
    print '|||          |||||||||||     |||     |||||||||   ||||||||||| |||          |||||||||||'
    print '|||          |||||||||||     |||     |||||||||   ||||||||||| |||          |||||||||||'
    print '|||          |||     |||     |||     |||   ||||  |||     ||| |||          |||     |||'
    print '|||          |||     |||     |||     |||    |||  |||     ||| |||          |||     |||'
    print '||||         |||     |||     |||     |||    |||  |||     ||| ||||         |||     |||'
    print ' |||||||||   |||     |||     |||     |||     ||| |||     |||  |||||||||   |||     |||'
    print '  |||||||||  |||     |||     |||     |||     ||| |||     |||   |||||||||  |||     |||'
    print '    CONTROLE    ADMINISTRATIVO    DE    TRAFEGO    ACADEMICO    AUTOMATIZADO'
    print '                        © 2015-2016  www.catraca.unilab.edu.br'
    
    try:
        Logs().main()
        Inicializador().start()
    except Exception:
        Logs().logger.error("Exception", exc_info=True)
    