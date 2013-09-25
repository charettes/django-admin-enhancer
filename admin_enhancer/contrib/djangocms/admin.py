from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured

from ...admin import EnhancedModelAdminMixin

try:
    from cms.admin.pageadmin import PageAdmin, Page

    class EnhancedPageAdmin(EnhancedModelAdminMixin, PageAdmin):
        pass

    admin.site.unregister(Page)
    admin.site.register(Page, EnhancedPageAdmin)
except ImportError:
    raise ImproperlyConfigured("Error while importing django-cms, please check your configuration")
