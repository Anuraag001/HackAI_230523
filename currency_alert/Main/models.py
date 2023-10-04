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
    