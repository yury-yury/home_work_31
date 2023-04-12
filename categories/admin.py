from django.contrib import admin

from categories.models import Category


admin.site.register(Category)

prepopulated_fields = {"slug": ("name",)}
