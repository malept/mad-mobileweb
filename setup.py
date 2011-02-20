#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(name='madpub',
      version='0.1',
      description='MadPub.org Mobile Web application',
      author='Mark Lee',
      packages=find_packages(),
      install_requires=[
          'django >= 1.3',
          'django-html5',
          'webassets',
      ])
