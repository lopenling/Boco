# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='Boco',
    version='v0.3.2',
    description='A corpus manager for Tibetan Language',
    long_description='Boco corpus manager is used for building, maintaining, and using corpora. The motivation is to make it as straightforward as possible to manage multiple corpora per project, as well as perform cross-corpus operations between those corpora.',
    url='https://github.com/lopenling/boco',
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
