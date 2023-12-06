from django.db import models
from django.contrib.auth.models import AbstractUser
class City(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'


class CustomUser(AbstractUser):
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

class Mall(models.Model):
    address = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    city = models.ManyToManyField(City)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'mall'
        verbose_name_plural = 'malls'
