#! /usr/bin/env python
from setuptools import setup
"""
`flasktool create ext`
    Console prompts to create a skeleton for a new extension. Adapted from 
    https://github.com/imlucas/flask-tool
"""

setup(
    name='Flask-Tool',
    version='0.1.2',
    url='https://github.com/johnvey/flask-tool',
    license='BSD',
    author='J Hwang',
    author_email='code@johnvey.com',
    description='Some tooling for developing with flask.',
    long_description=__doc__,
    packages=['flasktool'],
    namespace_packages=['flasktool'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'Flask-Script',
        'Jinja2'
    ],
    test_suite='test_tool',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points = {
        'console_scripts': [
            'flasktool = flasktool.console:run'
        ],
    }
)

