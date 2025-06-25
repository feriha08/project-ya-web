from django.contrib import admin

# Register your models here.
from .models import CreatureCard, Booking, CustomerProfile,Payment

admin.site.register(CreatureCard)
admin.site.register(Booking)
admin.site.register(CustomerProfile)
admin.site.register(Payment)





# @admin.register(Payment)
# class PaymentAdmin(admin.ModelAdmin):
#     list_display = ('booking', 'amount', 'payment_method', 'status', 'payment_date')
