from django.contrib import admin

# Register your models here.
from .models import Customer, Car, Booking

#
from django.contrib.auth.admin import UserAdmin
from .forms import CustomerCreationForm, CustomerChangeForm

admin.site.register(Booking)
admin.site.register(Car)


class CustomUserAdmin(UserAdmin):
    model = Customer
    add_form = CustomerCreationForm
    form = CustomerChangeForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('driver_license', 'birth_date', 'phone',)}),
    )


admin.site.register(Customer, CustomUserAdmin)
