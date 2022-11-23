#!/usr/bin/env python

from distutils.core import setup

setup(
    name='calam-voyager',
    version='1.0.0',
    description='Python package for interacting with Yardi Voyager.',
    author='Jason G',
    author_email='groverj324@gmail.com',
    url='https://github.com/groverj324/calam-voyager',
    packages=['calam_voyager', 'calam_voyager.blocking'],
    install_requires=[
        'aiohttp',
        'requests',
        'beautifulsoup4'
    ]
)