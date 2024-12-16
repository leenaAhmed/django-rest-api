from django.db import models



class MenuItem(models.Model):
    title= models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5 , decimal_places=2)
    inventory = models.SmallIntegerField()


class Book(models.Model):
    title= models.CharField(max_length=255)
    author= models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5 , decimal_places=2)
    inventory = models.SmallIntegerField(null=True , default=1)
    class Meta:
        indexes = models.Index(fields=['price']),

