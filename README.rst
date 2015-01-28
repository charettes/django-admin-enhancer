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

A simple django app that provides change and deletion links to FK fields
in the admin while ticket
`#13163 <https://code.djangoproject.com/ticket/13163>`__ and
`#13165 <https://code.djangoproject.com/ticket/13165>`__ are not fixed.

Note that this apps works with django >= 1.4 only.

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

Django CMS support
------------------

Django CMS (https://www.django-cms.org/) defines a plugin system to
create pluggable applications; its plugin system relies on standard
Django admin framework so it's easy to *enhance* plugins using this
project.

Plugin enhancement
~~~~~~~~~~~~~~~~~~

To add ``admin_enhancer`` support to your own plugins just add
``admin_enhancer.EnhancedAdminMixin`` to plugin class definition.

.. code:: python

    ...
    from admin_enhancer.admin import EnhancedAdminMixin

    class MyOwnPlugin(EnhancedAdminMixin, CMSPluginBase):
        name = "whatever"

        ...
    plugin_pool.register_plugin(MyOwnPlugin)

To *enhance* third party plugins, unregister original plugin and extend
it with your own base class.

.. code:: python

    ...
    from other.app.cms_plugins import ThirdPartyPlugin
    from admin_enhancer.admin import EnhancedAdminMixin

    class EnhancedThirPartyPlugin(EnhancedAdminMixin, ThirdPartyPlugin):
        pass

        ...
    plugin_pool.unregister_plugin(ThirdPartyPlugin)
    plugin_pool.register_plugin(EnhancedThirPartyPlugin)

Page admin support
~~~~~~~~~~~~~~~~~~

Django CMS defines a ModelAdmin for its ``Page`` object;
``admin_enhancer.contrib.djangocms`` defines a new ``ModelAdmin`` for
``Page`` to enhance it. To install it add
``admin_enhancer.contrib.djangocms`` to ``INSTALLED_APPS``, *after* any
``django-cms`` or ``django-admin-enhancer``-related application.

Django Filer support
--------------------

``django-filer`` (https://github.com/stefanfoulis/django-filer) has its
own *enhanced* widget which conflicts with ``django-admin-enhancer``; to
*enhance* filer-based applications, use ``enhance_exclude`` attribute on
your ModelAdmin to exclude filer-based fields from *enhancement* while
allowing other fields to be enriched.

``cmsplugin_filer`` (https://github.com/stefanfoulis/cmsplugin-filer)
can be extended to support ``django-admin-enhancer`` like any other
django CMS plugin; for better support ``admin_enhancer.contrib.filer``
defines a new ``ModelAdmin`` for ``ThumbnailOption`` class. To install
it add ``admin_enhancer.contrib.filer`` to ``INSTALLED_APPS``, *before*
``admin_enhancer.contrib.djangocms``.
