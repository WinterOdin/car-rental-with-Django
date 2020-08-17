from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Car)
admin.site.register(Faq)
admin.site.register(Year)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Location)
admin.site.register(Additions)
admin.site.register(canceledOrders)