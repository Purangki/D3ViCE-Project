# from D3ViCE_Conference.models import Conference
# from django.db.models.expressions import F
# from django.db.models.fields import DateField, DateTimeField, FloatField
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Profile(AbstractUser):
	is_deleted = models.BooleanField(default = False)
	avatar_index = models.IntegerField(null = True, blank = True)
	affiliation = models.CharField(max_length = 255, null = True, blank = True)
	display_name = models.CharField(max_length = 255, null = True, blank = True)

	is_host = models.BooleanField(default=False)
	is_sponsor = models.BooleanField(default=False)
	is_speaker = models.BooleanField(default=False)
	
	class Meta:
		db_table = "Profile"

# additional models

class Plan(models.Model):
	user = models.OneToOneField(Profile, on_delete=models.SET_NULL, null=True)
	is_paid = models.BooleanField(default = False)
	is_expired = models.BooleanField(default =  False)
	start = models.DateTimeField()
	end = models.DateTimeField()
	type = models.CharField(max_length = 150, null = True, blank = True ) #free, basic, premium
	cost_per_month = models.FloatField()

	class Meta:
		db_table = "Plan"

class Notification(models.Model):
	user = models.ManyToManyField(Profile)
	type = models.CharField(max_length = 255)
	description = models.CharField(max_length = 300)
	date = models.DateField()
	status = models.BooleanField(default = False) #Read and Unread


	class Meta:
		db_table = "Notification"

class Request(models.Model):
	user = models.ForeignKey(Profile, blank=True, on_delete=models.SET_NULL, null=True)
	type = models.CharField(max_length = 255) # Sponsor, Join
	description = models.CharField(max_length = 300)
	date = models.DateField()
	status = models.CharField(max_length=10, default = 'Pending') # Accepted or Declined or Pending

	class Meta:
		db_table = "Request"

