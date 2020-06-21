#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import io
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

DESCRIPTION = 'Collectd rabbitmq plugin'

try:
    with io.open('README.md', encoding='utf-8') as f:
        long_description = '\n' + f.read()
except OSError as e:
    if e.errno == errno.ENOENT:
       long_description = DESCRIPTION
    else:
        raise

setup(
    name='collectd-rabbitmq',
    version='1.0',
    description="A collected plugin, written in python, to"
                "collect statistics from RabbitMQ.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="apassionatechie",
    author_email='apassionatechie@gmail.com',
    url='https://github.com/aratik711/collectd_rabbitmq',
    packages=[
        'collectd_rabbitmq',
    ],
    package_dir={'collectd_rabbitmq': 'collectd_rabbitmq'},
    include_package_data=True,
    zip_safe=False,
    keywords='collectd-rabbitmq',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
    data_files=[('share/collectd/', ['config/rabbitmq.types.db'])],
)
