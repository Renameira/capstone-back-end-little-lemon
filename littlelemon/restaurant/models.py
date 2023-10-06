from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=50)
    no_of_guests = models.IntegerField()
    bookingdate = models.DateTimeField()


class MenuItens(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2,)
    invetory = models.IntegerField
