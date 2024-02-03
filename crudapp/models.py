from django.db import models

# Create your models here.

from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    author = models.CharField(max_length=250, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='pics')
    quantity = models.IntegerField()

    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


