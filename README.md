# django-admin-enhancer

## Overview

A simple django app that provides change and deletion links to FK fields in the admin while ticket [#13163](https://code.djangoproject.com/ticket/13163) and [#13165](https://code.djangoproject.com/ticket/13165) are not fixed.

## Display

![selected](https://dl.dropbox.com/u/2759157/selected.png)

![selected](https://dl.dropbox.com/u/2759157/empty.png)

[Video displaying interaction with the widget](https://www.youtube.com/watch?v=H4xqku-BPBU)

## Usage

Make sure to mix `admin_enhancer.EnhancedModelAdminMixin` when dealing with `django.contrib.admin.ModelAdmin` subclasses and `admin_enhancer.EnhancedAdminMixin` when dealing with `django.contrib.admin.InlineModelAdmin` at both ends of the relationship.

If edition and deletion controls appears but the popup is not closed nor is the select box updated your `ModelAdmin` subclass referenced by the field in question is probably not mixed with `admin_enhancer.EnhancedModelAdminMixin`.

For some examples take a look [here](https://github.com/charettes/django-admin-enhancer/blob/master/tests/test_app/admin.py).
