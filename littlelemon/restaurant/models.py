from django.db import models

# Create your models here.

class Booking(models.Model) :
    # id = models.IntegerField()
    name = models.CharField(max_length=255, db_index=True)
    no_of_guests = models.IntegerField()
    booking_date = models.DateField(db_index=True)


class MenuItem(models.Model) :
    # id = models.IntegerField()
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    inventory = models.IntegerField()