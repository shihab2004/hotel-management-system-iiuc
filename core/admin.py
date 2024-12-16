from django.contrib import admin
from core.models import *
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.db.models import Max

    
    
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("pk",'hotel','total_price',"paid_amount",'status')
    list_filter  = ['status',]
    change_list_template = "admin/change_booking_list.html"
    
    
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}

        extra_context['total_income'] = Booking.objects.aggregate(Max("paid_amount"))["paid_amount__max"]

        return super().changelist_view(request, extra_context=extra_context)



admin.site.register(Hotel)
admin.site.register(Room)