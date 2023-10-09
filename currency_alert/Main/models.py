from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    phone_number=models.BigIntegerField(null=True)
    def __str__(self):
        return self.first_name + " " + self.last_name



class User_Agent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name=models.CharField(max_length=30)
    base_currency = models.CharField(max_length=255)
    min_value = models.DecimalField(max_digits=10, decimal_places=2)
    max_value = models.DecimalField(max_digits=10, decimal_places=2)
    foreign_currency = models.CharField(max_length=255)

    def __str__(self):
        return self.base_currency  + " " + self.foreign_currency
    
class Alert(models.Model):
    base_currency = models.CharField(max_length=3)
    min_amount = models.DecimalField(max_digits=10, decimal_places=2)
    max_amount = models.DecimalField(max_digits=10, decimal_places=2)
    to_currency = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.base_currency} - {self.min_amount} to {self.max_amount} ({self.to_currency})"
    
class Forget(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100,null=True)