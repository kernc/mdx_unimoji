#!/usr/bin/env python

from setuptools import setup
import doctest

MODULE = 'mdx_unimoji'

tests = lambda: doctest.DocTestSuite(MODULE)

setup(
    name=MODULE,
    version='1.0',
    author='Jack Nicholson',
    author_email='kern.ce.ce++@gmail.com',
    description='Python-Markdown extension that replaces common smileys with their Unicode emoji emoticons. ;)',
    long_description_markdown_filename='README.md',
    url='https://github.com/kernc/' + MODULE,
    py_modules=[MODULE],
    test_suite='setup.tests',
    install_requires=['Markdown'],
    setup_requires=['setuptools-markdown'],
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
