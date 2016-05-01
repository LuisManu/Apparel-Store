#!/usr/bin/env python

from setuptools import setup

setup(
    # GETTING-STARTED: set your app name:
    name='ApparelWebStore',
    # GETTING-STARTED: set your app version:
    version='1.0',
    # GETTING-STARTED: set your app description:
    description='Apparel web app',
    # GETTING-STARTED: set author name (your name):
    author='L.M. Gutierrez',
    # GETTING-STARTED: set author email (your email):
    author_email='luismanugutierrez@gmail.com',
    # GETTING-STARTED: set author url (your url):
    url='http://luismanu.com',
    # GETTING-STARTED: define required django version:
    install_requires=[
        'Django==1.8.4'
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/'
    ],
)
