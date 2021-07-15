from django.db import models
from datetime import datetime
# from django.contrib.auth.models import auth, User
# from D3ViCE_User.models import Participant
# from D3ViCE_User.models import Sponsor
# from D3ViCE_User.models import Host
# from D3ViCE_User.models import Speaker
from D3ViCE_User.models import Profile
# # Create your models here.

class Conference(models.Model):
	code = models.CharField(max_length = 50)	#conference code
	title = models.CharField(max_length = 150)	#conference title
	date = models.DateField()	#conference start date
	time = models.TimeField()	#conference start time
	end_date = models.DateField(null = True, blank = True)	#conference end date
	end_time = models.TimeField(null = True, blank = True) 	#conference end time
	description = models.CharField(max_length = 255)	#conference description 
	is_deleted = models.BooleanField(default = False)	#archives the conference, deleted in the page but not in the db
	status = models.CharField(max_length = 50, default = "Upcoming")	#added by Abby for the main dashboard
	seats = models.IntegerField()
	type = models.CharField(max_length = 255)

	sponsor = models.ManyToManyField(Profile, related_name = 'sponsored_conferences', blank = True)
	host = models.ForeignKey(Profile, on_delete=models.SET_NULL, related_name="created_conferences", null=True, blank = True)
	participant = models.ManyToManyField(Profile, related_name = "joined_conferences", blank = True)
	speaker = models.ManyToManyField(Profile, related_name = "speaker_conferences", blank = True)

	class Meta:
		db_table = "Conference"

class Review(models.Model):
	user = models.ForeignKey(Profile, related_name="event_reviews",blank=True, on_delete=models.SET_NULL, null=True)
	conference = models.ForeignKey(Conference, related_name="event_reviews", blank=True, on_delete=models.SET_NULL, null=True)
	rating = models.IntegerField()
	feedback = models.CharField(max_length = 300) #description why mao na ang rating
	date = models.DateField()

	class Meta:
		db_table = "Review"