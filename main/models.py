from django.db import models
from django import forms

class UserData(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class AccountDetails(models.Model):
	user = models.ForeignKey(UserData, on_delete=models.CASCADE)
	website = models.CharField(max_length=200, null = True)
	logindetail = models.CharField(max_length=200)
	password = models.CharField(max_length=200)

	def __str__(self):
		return self.website+" Password Details"