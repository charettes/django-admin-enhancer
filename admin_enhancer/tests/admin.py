from django.contrib import admin

from .. import admin as enhanced_admin

from .models import Author, Book, Character, Theme


class EnhancedModelAdmin(enhanced_admin.EnhancedModelAdminMixin,
                         admin.ModelAdmin):
    pass

class CharacterInline(enhanced_admin.EnhancedAdminMixin,
                      admin.TabularInline):
    model = Character

class BookAdmin(EnhancedModelAdmin):
    inlines = (CharacterInline,)
    filter_horizontal = ('themes',)


admin.site.register(Author, EnhancedModelAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Theme, EnhancedModelAdmin)
