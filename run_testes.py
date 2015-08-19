#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

#from testes.testehorarios import TesteHorarios
from testes import tipo_teste
from testes import perfil_teste
from testes import cartao_teste
from testes import registro_teste
from testes import catraca_teste
from testes import giro_teste
from testes import turno_teste
from testes import mensagem_teste
from testes import finalidade_teste
from catraca.restful.servidor import app


__author__ = "Erivando Sena" 
__copyright__ = "Copyright 2015, Universidade da Integracao Internacional da Lusofonia Afro-Brasileira"
__email__ = "erivandoramos@unilab.edu.br"
__status__ = "Prototype" # Prototype | Development | Production


if __name__ == '__main__':
    
    #usuario_teste.main()
    #tipo_teste.main()
    #perfil_teste.main()
    #cartao_teste.main()
    #giro_teste.main()
    #turno_teste.main()
    #mensagem_teste.main()
    #catraca_teste.main()
    #finalidade_teste.main()
    #registro_teste.main()
    app.run(host='192.168.1.253', port=8089, debug=True)
    pass
