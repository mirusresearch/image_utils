#!/usr/bin/env python
from distutils.core import setup

setup(
    name='image_utils',
    version='1.0.1',
    description='Mirus Image Utilities',
    author='Frank Henard',
    author_email='frank@mirusresearch.com',
    packages=['image_utils'],
    install_requires=[
        'Pillow>=1.7.8',
    ]
)
