from django.contrib import admin

from products.models import Product, Specification, Field, Category

admin.site.register(Product)
admin.site.register(Specification)
admin.site.register(Category)
admin.site.register(Field)
