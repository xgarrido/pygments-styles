#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name             = 'pygments-styles',
    version          = '0.1.0',
    description      = 'Several homemade Pygments style',
    long_description = open ('README.md').read (),
    keywords         = ['pygments', 'style', 'syntax highlighting'],
    author           = "Xavier Garrido",
    author_email     = "xavier.garrido@gmail.com",
    url              = "https://github.com/xgarrido",
    install_requires = ['pygments >= 1.5'],
    packages         = find_packages (),
    entry_points     = '''
    [pygments.styles]
    upsud = pygments_styles.upsud:UPSUDStyle
    snemo = pygments_styles.snemo:SNEMOStyle
    '''
    )
