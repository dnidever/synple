#!/usr/bin/env python

import os
import shutil
from setuptools import setup, find_packages, extension
from setuptools.command.install import install
#from numpy.distutils.core import setup, Extension


class PreInstallCommand(install):
        """Pre-installation for installation mode."""
        def run(self):
                # Step 1. Compile fortran code
                os.system('cd synspec; make; cd ..')
                # Step 2. Download the linelist
                
                
class PostInstallCommand(install):
        """Post-installation for installation mode."""
        def run(self):
                # Step 3. Copy binaries to scripts directory
                
                synspec = 'bin/s54d'
                if os.path.exists(synspec):
                        self.copy_file(synspec,self.install_scripts)
                rotin = 'bin/rotin3'
                if os.path.exists(rotin):
                        self.copy_file(rotin,self.install_scripts)
                

#mod = extension.Extension(name = 's54d', sources = ['synspec/s54d.f'])
#mod = Extension(name = 's54d', sources = ['synspec/s54d.f'])
setup(name='synple',
      version='1.0',
      description='An Easy-to-Use Python Wrapper for the Spectral Synthesis Code Synspec',
      author='Carlos Allende Prieto',
      author_email='callende@iac.es',
      url='https://github.com/callendeprieto/synple',
      packages=find_packages(),
      #ext_modules = [mod],
      scripts=['bin/synple'],
      requires=['numpy','astropy(>=4.0)','scipy'],
      include_package_data=True,
      #cmdclass={'install': PostInstallCommand},
      #package_data={'synple': ['data/']},
)
