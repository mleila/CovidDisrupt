import os
from distutils.core import setup

scripts = [os.path.join('bin', f) for f in os.listdir('./bin')]
packages = ['covid', 'covidash']

setup(name='covid',
      version='0.1',
      scripts=scripts,
      packages=packages
      )
