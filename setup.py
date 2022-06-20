#!/usr/bin/env python
import doctest
from pathlib import Path

from setuptools import setup

MODULE = 'mdx_unimoji'


def tests():
    doctest.DocTestSuite(MODULE)


with open(Path(__file__).parent / 'README.md') as readme_file:
    readme = '\n' + readme_file.read()

setup(
    name=MODULE,
    version='1.1',
    author='Jack Nicholson',
    author_email='kern.ce.ce++@gmail.com',
    description='Python-Markdown extension that replaces common smileys with their Unicode emoji emoticons. ;)',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/kernc/' + MODULE,
    py_modules=[MODULE],
    test_suite='setup.tests',
    install_requires=['Markdown'],
    license='GPLv3+',
    keywords='markdown unicode emoji emoticon',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
