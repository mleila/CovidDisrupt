import os
from distutils.core import setup

scripts = [f for f in os.listdir('./bin')]
packages = ['covid']

setup(name='covid',
      version='0.1',
      scripts=scripts,
      packages=packages
      )
