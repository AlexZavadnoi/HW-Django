from django.contrib import admin
from django.apps import apps
from .models import Books, Authors, Profile


class BooksAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Books._meta.fields]
    search_fields = ['title', 'id', 'author__last_name']
    list_filter = ['title', 'author_id', 'author__last_name']
    list_editable = ['title', ]


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Authors)
admin.site.register(Profile)
admin.site.register(Books, BooksAdmin)
