from django.db import models

# Create your models here.
class Menu(models.Model):
    Title = models.CharField(max_length=1)
    Price = models.DecimalField(max_digits=6, decimal_places=2)
    Inventory = models.IntegerField()

    def __str__(self):
        return f'{self.Title}: {str(self.Price)}'


class Booking(models.Model):
    Name = models.CharField(max_length=100)
    No_of_guests = models.PositiveIntegerField()
    BookingDate = models.DateField()

    def __str__(self):
        return f'{self.Name} - {self.BookingDate}'
