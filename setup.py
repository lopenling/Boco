# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='Bocor',
    version='v0.3',
    description='A Corpus Manager for Tibetan Language',
    long_description='A Corpus Manager for Tibetan Language',
    url='https://github.com/lopenling/bocor',
    author='Mikko Kotila',
    author_email='mailme@mikkokotila.com',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='language corpus linguistics tibetan',
    packages=find_packages(),
)