from django.contrib import admin
from django.db.models.base import Model
from .models import Book

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
    list_filter = ("author", "rating", )
    list_display = ("title", "author", )


admin.site.register(Book, BookAdmin)
