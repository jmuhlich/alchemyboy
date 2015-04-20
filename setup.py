#!/usr/bin/env python
"""alchemyboy package config."""

import codecs
import os
from setuptools import setup

import alchemyboy


dirname = os.path.dirname(__file__)

long_description = (
    codecs.open(os.path.join(dirname, "README.rst"), encoding="utf-8").read() + "\n" +
    codecs.open(os.path.join(dirname, "AUTHORS.rst"), encoding="utf-8").read() + "\n" +
    codecs.open(os.path.join(dirname, "CHANGES.rst"), encoding="utf-8").read()
)

setup(
    name="alchemyboy",
    description="Automatic generation of the factory-boy factories for the SQLAlchemy models.",
    long_description=long_description,
    author="Oleg Pidsadnyi and others",
    license="MIT license",
    author_email="oleg.pidsadnyi@gmail.com",
    url="https://github.com/olegpidsadnyi/alchemyboy",
    version=alchemyboy.__version__,
    classifiers=[
        "Development Status :: 6 - Mature",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"
    ] + [("Programming Language :: Python :: %s" % x) for x in "2.6 2.7 3.0 3.1 3.2 3.3 3.4".split()],
    install_requires=[
        "factory_boy",
        "sqlalchemy",
    ],
    tests_require=["tox"],
    packages=["alchemyboy"],
    include_package_data=True,
)
