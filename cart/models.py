from django.db import models
from shop.models import *

# Create your models here.
class Cartlist(models.Model):
    cart_id=models.CharField(max_length=250)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class items(models.Model):
    prodt=models.ForeignKey(Products,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cartlist,on_delete=models.CASCADE)
    quan=models.IntegerField()
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.prodt

    def total(self):
        return self.prodt.price*self.quan
