from django.contrib import admin

from accounts.models import Vendor, Buyer, Charge

admin.site.register(Vendor)
admin.site.register(Buyer)
admin.site.register(Charge)
