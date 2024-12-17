from django.db import models

class Category(models.Model):
    slug= models.SlugField(unique=True)
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title
    
class MenuItem(models.Model):
    title= models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5 , decimal_places=2)
    inventory = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1, null=True)


class Book(models.Model):
    title= models.CharField(max_length=255)
    author= models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5 , decimal_places=2)
    inventory = models.SmallIntegerField(null=True)
    class Meta:
        indexes = models.Index(fields=['price']),

