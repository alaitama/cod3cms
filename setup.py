#!/usr/bin/env python

from setuptools import setup

setup(
    name='cod3-mezzanine-openshift',
    version='1.0',
    description='COD3 web. Mezzanine configured for deployment on OpenShift.',
    author='Alberto Laita',
    author_email='alblaita@gmail.com',
    url='http://ramsys.es/',
    install_requires=[
        'Django==1.6.11',
        'mezzanine==3.1.10',
        'django_compressor==1.5',
        'django-storages==1.1.8',
        'boto==2.38.0'
    ],
)
