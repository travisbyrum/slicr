# -*- coding: utf-8 -*-

import re
from setuptools import setup, find_packages


_version_re = re.compile(r'__version__\s+=\s+(.*)')


with open('slicr/__init__.py', 'r', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)


setup(
    name='slicr',
    version=version,
    author='Travis Byrum',
    author_email='travis.tbyrum@gmail.com',
    maintainer='Travis Byrum',
    maintainer_email='travis.tbyrum@gmail.com',
    description='URL shortener application.',
    license='MIT',
    packages=find_packages(exclude=('tests')),
    include_package_data=True,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'slicr = slicr.cli:main'
        ]
    }
)
