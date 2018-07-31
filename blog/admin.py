from django.contrib import admin

from .models import Blog, Category, Tag

admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(Category)
