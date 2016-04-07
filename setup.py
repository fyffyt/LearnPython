#!/usr/bin/env python
#-*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='qa-lib',
    version='0.2.1',
    description='TestLibs of qa',
    author='jolyon',
    url='www.percolata.com',
    license='GPL',
    packages=find_packages("."),
    scripts=["scripts/haha"],
    install_requires=[
        'azure==1.0.2',
        'beautifulsoup4>=4.0.0',
        'boto>=2.0.0',
        'lxml>=3.0.0',
        'pexpect>=3.0',
        'protobuf>=2.0.0',
        'protobuf-to-dict>=0.1.0',
        'requests>=2.0.0'
        ],
    data_files=[
        ('TestConfig', [
            'TestConfig/config',
            'TestConfig/keys',
            'TestConfig/list_test'
            ]
            )
        ],
    dependency_links=[]
)
