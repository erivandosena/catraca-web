#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os, sys

from distutils.core import setup

setup(name='Distutils',
      version='1.0',
      description='Python Distribution Utilities',
      author='Erivando Sena',
      author_email='erivandoramos@unilab.edu.br',
      url='http://www.unilab.edu.br',
      packages=['distutils', 'distutils.command'],
     )
