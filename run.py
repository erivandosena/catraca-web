#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from catraca.logs import Logs
from catraca.painel import Painel


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Universidade da Integracao Internacional da Lusofonia Afro-Brasileira" 
__email__ = "erivandoramos@unilab.edu.br" 
__status__ = "Prototype" # Prototype | Development | Production 


if __name__ == '__main__':
    Logs().main()
    Painel().main()