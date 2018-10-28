from setuptools import setup
import os

setup(
    name='dalaran',
    packages=['dalaran'],
    version='0.1.0',
    description=' Basic Lexer and Parser for Hearthstone Cards',
    author='Kai Chang',
    author_email='kaijchang@gmail.com',
    url='https://github.com/kajchang/Dalaran',
    license='MIT',
    long_description=open(os.path.join(os.path.abspath(
        os.path.dirname(__file__)), 'README.md')).read(),
    long_description_content_type="text/markdown",
    install_requires=open(os.path.join(os.path.abspath(
        os.path.dirname(__file__)), 'requirements.txt')).readlines()
)
