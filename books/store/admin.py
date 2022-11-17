from django.contrib import admin
from django.contrib.admin import ModelAdmin

from store.models import Book, UserBookRelations


@admin.register(Book)
class BookAdmin(ModelAdmin):
    pass


@admin.register(UserBookRelations)
class UserBookRelationsAdmin(ModelAdmin):
    pass
