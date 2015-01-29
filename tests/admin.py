from __future__ import unicode_literals

from django.contrib.admin import AdminSite, ModelAdmin, TabularInline

from admin_enhancer import admin as enhanced_admin

from .models import Author, Book, Character, Theme


site = AdminSite()


class EnhancedModelAdmin(enhanced_admin.EnhancedModelAdminMixin, ModelAdmin):
    pass


class CharacterInline(enhanced_admin.EnhancedAdminMixin, TabularInline):
    model = Character


class BookAdmin(EnhancedModelAdmin):
    inlines = (CharacterInline,)
    filter_horizontal = ('themes',)


site.register(Author, EnhancedModelAdmin)
site.register(Book, BookAdmin)
site.register(Theme, EnhancedModelAdmin)
