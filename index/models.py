from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
	amount = models.CharField(max_length=30)
	lastpayment = models.CharField(max_length=30, default="90.892.00")

	def __str__(self):
		return self.username
