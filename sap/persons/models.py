from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=255)
    num_street = models.IntegerField()
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"Address {self.id}: {self.street}: {self.num_street}: {self.country}"

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"person {self.id} {self.name} {self.last_name} {self.email}: "