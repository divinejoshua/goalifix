from django.contrib import admin
from .models import Products, Bidder, BidStatus
# Register your models here.

admin.site.register(Products)
admin.site.register(Bidder)
admin.site.register(BidStatus)
