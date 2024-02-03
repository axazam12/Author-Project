from django.db import models
from django.urls import reverse
from authapp.models import UserProfile
from crudapp.models import Book
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    items=models.ManyToManyField(Book)

class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)

    # def get_absolute_url(self):
    #     return reverse('checkout_session', args=[str(self.id)])