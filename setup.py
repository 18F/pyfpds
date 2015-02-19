#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.md').read()

requirements = [
    # TODO: put package requirements here
    'xmltodict',
    'requests',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pyfpds',
    version='0.1.0',
    description='pyfpds is a python wrapper for accessing federal contracting data in the Federal Procurement Data System (FPDS)',
    long_description=readme,
    author='Kaitlin Devine',
    author_email='kaitlin.devine@gsa.gov',
    url='https://github.com/kaitlin/pyfpds',
    packages=[
        'pyfpds',
    ],
    package_dir={'pyfpds':
                 'pyfpds'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='pyfpds',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
