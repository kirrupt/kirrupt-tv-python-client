#!/bin/env python

from setuptools import setup

VERSION = __import__("kirrupt_tv").__version__

setup(
    name='kirrupt-tv',
    version=VERSION,
    description='A Python client for the Kirrupt TV API.',
    install_requires=[
        'requests',
    ],
    author='Kirrupt',
    author_email='info@kirrupt.com',
    url='https://github.com/kirrupt/kirrupt-tv-python-client',
    license='MIT',
    packages=['kirrupt_tv'],
    package_data={'': []},
    classifiers=(
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)