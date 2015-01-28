#!/usr/bin/python
from __future__ import unicode_literals

from setuptools import find_packages, setup

from admin_enhancer import __version__


with open('README.rst') as file_:
    long_description = file_.read()

setup(
    name='django-admin-enhancer',
    version='.'.join(str(v) for v in __version__),
    description='A simple django app that provides change and deletion links to FK fields in the admin.',
    long_description=long_description,
    url='https://github.com/charettes/django-admin-enhancer',
    author='Simon Charette',
    author_email='charette.s+admin-enhancer@gmail.com',
    license='MIT License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    include_package_data=True,
    keywords=['django admin foreign'],
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=['django>=1.4,<1.8'],
)
