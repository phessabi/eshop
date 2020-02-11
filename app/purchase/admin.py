from django.contrib import admin

from purchase.models import Cart, Payment, Order

admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Payment)
