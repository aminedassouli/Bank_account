#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importations
# ------------
from setuptools import find_packages, setup


# Package meta-data
# -----------------
NAME = 'Bank Account or Service complaints'
DESCRIPTION = ''
EMAIL = 'aminedassouli@gmail.com'
AUTHOR = 'Mohamed Amine Dassouli'
REQUIRES_PYTHON = '>=3.6.0'


# Required packages
# -----------------
REQUIRED = [
    "pandas",
    "notebook",
    "matplotlib"
]


# Where the magic happens
# -----------------------
setup(
    name=NAME,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(),
    install_requires=REQUIRED,
    include_package_data=True
)
