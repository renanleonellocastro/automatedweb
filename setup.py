# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='automatedweb',
    version='1.0.0',
    url='https://github.com/renanleonellocastro/automatedweb.git',
    license='MIT License',
    author='Renan Leonello Castro',
    author_email='renanleonellocastro@gmail.com',
    keywords='automatedweb web automated post get requests rest restfull',
    description=u'A tool to make it easy to communicate with web systems writting and reading data from them',
    install_requires=[
        "requests>=2.22.0",
        "pyquery>=1.4.0",
        "json5>=0.8.5",
        "urllib3>=1.25.10",
    ],
)
