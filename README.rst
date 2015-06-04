django-admin-enhancer
=====================

.. image:: https://travis-ci.org/charettes/django-admin-enhancer.svg?branch=master
    :target: https://travis-ci.org/charettes/django-admin-enhancer
    :alt: Build Status

.. image:: https://coveralls.io/repos/charettes/django-admin-enhancer/badge.svg?branch=master
    :target: https://coveralls.io/r/charettes/django-admin-enhancer?branch=master
    :alt: Coverage Status

Overview
--------

A simple django app that provided change and deletion links to FK fields
in the admin before tickets
`#13163 <https://code.djangoproject.com/ticket/13163>`__ and
`#13165 <https://code.djangoproject.com/ticket/13165>`__ were fixed.

Note that this apps works with 1.4 <= Django < 1.8 since both ticket have been solved and merged into Django 1.8.

Display
-------

.. figure:: https://dl.dropbox.com/u/2759157/selected.png
   :alt: Selected

   selected
.. figure:: https://dl.dropbox.com/u/2759157/empty.png
   :alt: Empty

Usage
-----

The recommended way to install ``django-admin-enhancer`` is via
`pip <http://www.pip-installer.org/>`__:

.. code:: sh

    pip install django-admin-enhancer

Add ``'admin_enhancer'`` to your ``INSTALLED_APPS`` to avoid getting
``TemplateDoesNotExist`` errors.

Make sure to mix ``EnhancedModelAdminMixin`` when dealing with
``django.contrib.admin.ModelAdmin`` subclasses and
``EnhancedAdminMixin`` when dealing with
``django.contrib.admin.InlineModelAdmin`` at both ends of the
relationship. The mixins are located at ``admin_enhancer.admin``.

If edition and deletion controls appears but the popup is not closed nor
is the select box updated your ``ModelAdmin`` subclass referenced by the
field in question is probably not mixed with
``EnhancedModelAdminMixin``.

For some examples take a look
`here <https://github.com/charettes/django-admin-enhancer/blob/master/tests/admin.py>`__.
