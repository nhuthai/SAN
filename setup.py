#!/usr/bin/env python3

from setuptools import setup, find_packages


setup(
    name='SAN',
    version='0.0',
    author='Nhut Hai Huynh',
    author_email='nhut.h.huynh@fh-kiel.de',
    packages=find_packages(),
    install_requires=[
        'click',
        'colorama',
        'matplotlib',
        'natsort',
        'numpy',
        'scipy',
        'scikit-image',
        'SimpleITK',
        'voluptuous'
    ],
    entry_points='''
        [console_scripts]
        SAN=SAN.cli:main
    ''',
)
