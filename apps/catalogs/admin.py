from django.contrib import admin
from apps.catalogs.models import Product, Category, Comment

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Comment)
