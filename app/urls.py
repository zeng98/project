# -*- coding:utf8 -*-
from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
	# homepage
    path('', views.HomePageView.as_view(), name="home_page"), 
    # add booking order
    path('booking/<int:car_id>', views.add_booking, name="add_booking"),
    # derive booking list
    path('orders/<int:customer_id>', views.BookingListView.as_view(), name="booking_list"),
    # edit one booking order
    path('booking/edit/<int:pk>', views.booking_edit, name='booking_update'),
    # delete one booking order
    path('booking/delete/<int:pk>', views.delete_booking, name='booking_delete'),
    # register
    path('register/', views.register, name='register'),
    path('profile/<int:pk>', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('booking/all', views.AllBookingList.as_view(), name='all_booking'),  # list of booking for admin
]
