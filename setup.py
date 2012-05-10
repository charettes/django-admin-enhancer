#!/usr/bin/python
from setuptools import setup, find_packages

from admin_enhancer import __version__

github_url = 'https://github.com/charettes/django-admin-enhancer'
long_desc = open('README.md').read()

setup(
    name='django-admin-enhancer',
    version='.'.join(str(v) for v in __version__),
    description='Simple app that',
    long_description=long_desc,
    url=github_url,
    author='Simon Charette',
    author_email='charette.s@gmail.com',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    license='MIT License',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
