# https://betterprogramming.pub/how-to-design-relationships-between-your-django-models-caa01bc17a5c

from django.db import models

class Country(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CapitalCity(models.Model):
    country=models.OneToOneField(Country,
                                 on_delete=models.CASCADE,
                                 primary_key=True)
    name=models.CharField(max_length=50)
    def __str__(self) -> str:
        return super().__str__()