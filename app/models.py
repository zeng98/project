from django.db import models
from django.contrib.auth.models import AbstractUser


# inherit the built in user model: AbstractUser
# and extend it , add additional fields
class Customer(AbstractUser):
    # driver license
    driver_license = models.CharField(max_length=50, blank=True, null=True)
    # birth date of customer
    birth_date = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Car(models.Model):
    """
    car model
    """
    # name of the car
    name = models.CharField(max_length=200, verbose_name='name')
    type_choices = (('Economy', 'Economy'), ('Standard', 'Standard'),
                    ('Estate', 'Estate'), ('luxury', 'luxury'), ('SUV', 'SUV'),
    )
    # type the car
    type = models.CharField(max_length=20, choices=type_choices, null=True, blank=True)
    # image of car
    image = models.ImageField(upload_to='img/', null=True, blank=True)
    # production year
    year = models.IntegerField(verbose_name='production_year')
    # rental rate per hour
    hour_rate = models.FloatField(verbose_name='hour_rate')
    # created time
    created = models.DateTimeField(verbose_name='created_time', auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "car"
        verbose_name_plural = verbose_name
        ordering = ['-created']

    def __str__(self):
        """Return a string representation of this object."""
        return self.name[:50]


class Booking(models.Model):
    # customer who rent
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    # car to rent
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car')
    # pickup date
    pick_up_date = models.DateTimeField(null=True, blank=True, verbose_name='pick_up_time')
    # return date
    drop_off_date = models.DateTimeField(null=True, blank=True, verbose_name='return_time')
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = verbose_name
        ordering = ('pick_up_date',)

    def __str__(self):
        """Return a string representation of this object."""
        return str(self.id)

    def get_total_hours(self):
        # subtract the dates, yield a datetime.timedelta object
        dt = self.return_date - self.pickup_date
        # Returns number of hours between dates
        hours = dt.seconds / 60 / 60
        return hours

    def get_total_price(self):
        return self.get_total_hours() * self.car.hour_rate

