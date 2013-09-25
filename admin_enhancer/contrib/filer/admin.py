from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured

from ...admin import EnhancedModelAdminMixin

try:
    from cmsplugin_filer_image.admin import ThumbnailOption

    class EnhancedThumbnailOptionAdmin(EnhancedModelAdminMixin,
                                       admin.ModelAdmin):
        list_display = ('name', 'width', 'height')

    admin.site.unregister(ThumbnailOption)
    admin.site.register(ThumbnailOption, EnhancedThumbnailOptionAdmin)
except ImportError:
    raise ImproperlyConfigured("Error while importing cmsplugin_filer, please check your configuration")
