from django.contrib.auth.models import User
from django.db import models

from apps.clothing.models import ApparelInfo



class UserProfile(models.Model):
	user =  models.OneToOneField(User)
	likes = models.ManyToManyField(ApparelInfo, blank=True)

	def __unicode__(self):
		return self.user.username