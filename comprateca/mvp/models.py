from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django_facebook.models import FacebookProfileModel


class Profile(FacebookProfileModel):
	user = models.OneToOneField(User)

	def __unicode__(self):
		return u'%s' % self.user

	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	#Signal to create when new user
	post_save.connect(create_user_profile, sender=User)

class Article(models.Model):
	owner = models.ForeignKey(User)
	title = models.CharField(max_length=100)
	price = models.IntegerField()
	date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u'%s' % self.title

