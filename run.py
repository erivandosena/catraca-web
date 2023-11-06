#!/usr/bin/env python
# -*- coding: utf-8 -*-


from catraca.logs import Logs
from catraca.visao.interface.inicializador import Inicializador


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, © 09/02/2015" 
__email__ = "erivandoramos@bol.com.br" 
__status__ = "Prototype"


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
    