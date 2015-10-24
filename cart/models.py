from django.db import models
from django.contrib.auth.models import User

from clothing.models import ApparelInfo






class OrderTicket(models.Model):
	user = models.ForeignKey(User)
	product_name = models.ForeignKey(ApparelInfo)
	size = models.CharField(max_length=25)