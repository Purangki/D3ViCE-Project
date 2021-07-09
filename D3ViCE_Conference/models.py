from django.db import models
from datetime import datetime
from django.contrib.auth.models import auth, User
from D3ViCE_User.models import Participant
from D3ViCE_User.models import Sponsor
from D3ViCE_User.models import Organizer
from D3ViCE_User.models import Speaker
# # Create your models here.

class Conference(models.Model):
	code = models.CharField(max_length = 50)	#conference code
	title = models.CharField(max_length = 150)	#conference title
	date = models.DateField()	#conference start date
	time = models.TimeField()	#conference start time
	end_date = models.DateField()	#conference end date
	end_time = models.TimeField() 	#conference end time
	description = models.CharField(max_length = 255)	#conference description 
	is_deleted = models.BooleanField(default = False)	#archives the conference, deleted in the page but not in the db
	status = models.CharField(max_length = 50, default = "Not Started")	#added by Abby for the main dashboard

	sponsor = models.ManyToManyField(Sponsor, on_delete=models.CASCADE, related_name = 'sponsored_conferences', null = True, blank = True)
	organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE, related_name="created_conferences")
	participant = models.ManyToManyField(Participant, on_delete = models.CASCADE, related_name = "joined_conferences")
	speaker = models.ManyToManyField(Speaker, on_delete = models.CASCADE, related_name = "joined_conferences")

	class Meta:
		db_table = "Conference"
			