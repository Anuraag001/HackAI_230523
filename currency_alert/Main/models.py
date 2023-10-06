from django.db import models

# Create your models here.
class Customer(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=30)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    phone_number=models.BigIntegerField(null=True)
    def __str__(self):
        return self.first_name + " " + self.last_name


class Alert(models.Model):
    base_currency = models.CharField(max_length=3)
    min_amount = models.DecimalField(max_digits=10, decimal_places=2)
    max_amount = models.DecimalField(max_digits=10, decimal_places=2)
    to_currency = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.base_currency} - {self.min_amount} to {self.max_amount} ({self.to_currency})"

    