from django.views.generic import ListView, DetailView # new
from django.shortcuts import render, redirect
from .models import Car, Booking, Customer
from .forms import CustomerCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from datetime import datetime


# get list of car that we have
class HomePageView(ListView):
    model = Car  # set the list view model
    template_name = 'home.html'  # template which we need to render to user


# get list of order of one customer
class BookingListView(ListView):
    model = Booking  # set the model list view of booking order, which is the data sorce
    template_name = 'Booking_list.html' # template for list booking order

    def get_queryset(self):
        # overide the queryset function, to get the all orders of specific user
        return Booking.objects.filter(customer_id=self.request.user).order_by('-pick_up_date')


# delete view, using function 
# add a login required decorater, which means user need login before access this page
@login_required
def delete_booking(request, **kwargs):
    # if request http method is post
    if request.method == 'POST': 
        # delete the booking order by booking id which primary key send from post method
        Booking.objects.filter(id=request.POST['pk']).delete()
        # redirect user to booking orders page after deleted 
        return HttpResponseRedirect(reverse('app:booking_list', kwargs={'customer_id': request.user.pk}))

    else:
        # if get method, redirect to booking list page
        return HttpResponseRedirect(reverse('app:booking_list', kwargs={'customer_id': request.user.pk}))


@login_required
def add_booking(request, **kwargs):
    if request.method == 'POST':
        # process the data, convert string to datetime format
        drop_off_date = datetime.strptime(request.POST['drop_off_date'], "%H:%M %m/%d/%Y")
        pick_up_date = datetime.strptime(request.POST['pick_up_date'], "%H:%M %m/%d/%Y")
        # process the data, get car id from post
        car_id = request.POST['car_id']
        # process the data, get customer id from request
        customer_id = request.user.pk
        # orm to create a instance of model by customer_id , car_id, pickup and drop off date
        Booking.objects.create(customer_id=customer_id, car_id=car_id,
                               pick_up_date=pick_up_date, drop_off_date=drop_off_date)
        # redirect to booki list page after succeed
        return HttpResponseRedirect(reverse('app:booking_list', kwargs={'customer_id': request.user.pk}))
    else:
        # if get method, get auth user and car id from url
        customer = request.user
        car_id = kwargs['car_id']
        # orm to get a car by car_id
        car = Car.objects.filter(pk=car_id).first()
        # form context dict
        context = {'customer': customer, 'car': car}
        # render to user
        return render(request, 'add_booking.html', context)


# register user
def register(request):
    if request.method == 'POST':
        # bounded form from post
        form = CustomerCreationForm(request.POST)
        # if form is valid
        if form.is_valid():
            # save form data
            form.save()
            # redirect to home page
            return redirect('/')
    else:
        # if it is get method, unbound form sent to user
        form = CustomerCreationForm()
        # redirect form and template to user
    return render(request, 'registration/register.html', context={'form': form})

# update a order
@login_required
def booking_edit(request, **kwargs):
    if request.method == 'POST':
        # get boooking object by pk send from post 
        booking = Booking.objects.filter(id=request.POST['pk']).first()
        # convert date to datetime
        drop_off_date = datetime.strptime(request.POST['drop_off_date'], "%H:%M %m/%d/%Y")
        pick_up_date = datetime.strptime(request.POST['pick_up_date'], "%H:%M %m/%d/%Y")
        # update object fields
        booking.pick_up_date = drop_off_date
        booking.drop_off_date = pick_up_date
        # save object
        booking.save()
        # redirect user to booking list 
        return HttpResponseRedirect(reverse('app:booking_list', kwargs={'customer_id': request.user.pk}))
    else:
        # orm to get booking object by pk
        booking = Booking.objects.filter(id=kwargs['pk']).first()
        # render template and booking object to user
        return render(request, 'edit_booking.html', context={'booking': booking})


class AllBookingList(ListView):
    """
    #get list of all booking that we have
    """
    model = Booking  # set the list view model
    template_name = 'all_booking.html'  #  template which we need to render to user


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_profile.html'
