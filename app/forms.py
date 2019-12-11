from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Customer
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin


class CustomerCreationForm(UserCreationForm):

    class Meta:
        model = Customer
        fields = ('username', 'email', 'driver_license', 'birth_date', 'phone')


class CustomerChangeForm(UserChangeForm):

    class Meta:
        model = Customer
        fields = UserChangeForm.Meta.fields


