#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='synple',
      version='1.0',
      description='An Easy-to-Use Python Wrapper for the Spectral Synthesis Code Synspec',
      author='Carlos Allende Prieto',
      author_email='callende@iac.es',
      url='https://github.com/callendeprieto/synple',
      #packages=find_packages(exclude=["tests"]),
      scripts=['bin/synple','bin/s54d','bin/rotin3'],
      requires=['numpy','astropy(>=4.0)','scipy'],
      #include_package_data=True,
)
