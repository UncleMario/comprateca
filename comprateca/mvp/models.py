# -*- coding: UTF-8 -*-

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

	def get_url(self):
		return 'http://www.comprateca.com/mvp/article/%s' % self.pk

	def get_wall_message(self):
		return 'Estoy comprando: %s a $%s, vendemelo en este link %s' % (self.title, self.price, self.get_url())

	def get_twitter_message(self):
		return 'Estoy comprando: %s a $%s, vendemelo aquí --> ' % (self.title, self.price)




