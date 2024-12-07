from django.db import models

# Create your models here.
class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} - {self.booking_date}"


class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.FloatField()
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'

