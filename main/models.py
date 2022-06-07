from django.db import models
from django import forms

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class UserData(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(null=False, unique=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("userdata_detail", kwargs = {"slug": self.slug})


class AccountDetails(models.Model):
	user = models.ForeignKey(UserData, related_name="account_details", on_delete=models.CASCADE)
	username = models.CharField(max_length=200)
	website = models.CharField(max_length=200, null = True)
	logindetail = models.CharField(max_length=200)
	password = models.CharField(max_length=200)

	def __str__(self):
		return self.website+" Password Details" 


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)