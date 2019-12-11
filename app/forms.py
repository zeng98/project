from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Customer
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin


class CustomerCreationForm(UserCreationForm):
    '''A form to add new customer profile to the database.'''
    class Meta:
        '''Associate this form with the Customer model.'''
        model = Customer
        fields = ('username', 'email', 'driver_license', 'birth_date', 'phone')


class CustomerChangeForm(UserChangeForm):
    '''A form to change customer profile to the database.'''
    class Meta:
        '''Associate this form with the Customer model.'''
        model = Customer
        fields = UserChangeForm.Meta.fields


