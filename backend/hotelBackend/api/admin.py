from django.contrib import admin
from .models import SuperUser, Staff, Customer, Table, FoodCategory, Menu, Booking, Billing, BillingItem;

# Register your models here.
admin.site.register(SuperUser)
admin.site.register(Staff)
admin.site.register(Customer)
admin.site.register(Table)
admin.site.register(FoodCategory)
admin.site.register(Menu)   
admin.site.register(Booking)
admin.site.register(Billing)
admin.site.register(BillingItem)
