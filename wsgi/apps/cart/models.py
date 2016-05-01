from django.db import models
from django.contrib.auth.models import User

from apps.clothing.models import ApparelInfo






class ItemInCart(models.Model):
	user = models.ForeignKey(User)
	product_name = models.ForeignKey(ApparelInfo)
	size = models.CharField(max_length=25)



class ToBeShipped(models.Model):
	user = models.ForeignKey(User)
	items_to_be_shipped = models.TextField()