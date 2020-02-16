from django.contrib import admin

from purchase.models import Cart, Payment, Order, Campaign

admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Campaign)
