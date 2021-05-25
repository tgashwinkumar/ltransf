from os import name
from sys import version
from setuptools import _install_setup_requires, find_packages, setup

setup(
    name='transf',
    packages=find_packages(include=['transf']),
    version='0.1.0',
    description='My First Python Library',
    author='tg',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests'
)