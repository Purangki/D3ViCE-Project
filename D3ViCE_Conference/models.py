from django.db import models
from datetime import datetime
from django.contrib.auth.models import auth, User
from D3ViCE_User.models import Participant
from D3ViCE_User.models import Sponsor
# # Create your models here.

class Conference(models.Model):
	code = models.CharField(max_length = 50)	#conference code
	title = models.CharField(max_length = 150)	#conference title
	date = models.DateField()	#conference date
	time = models.TimeField()	#conference time
	description = models.CharField(max_length = 255)	#conference description 
	is_created = models.BooleanField(default = False) 	#True - user is host of (or created the) conference, False - user is just a participant
	is_deleted = models.BooleanField(default = False)	#archives the conference, deleted in the page but not in the db
	status = models.CharField(max_length = 50, default = "Not Started")	#added by Abby for the main dashboard
	participant = models.ManyToManyField(Participant)
	sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, related_name = 'sponsor', null = True, blank = True)
	# host = models.ForeignKey(Host, on_delete = models.SET_NULL, null = True, related_name = "all_conferences") #added by Abby 
	# speaker = models.ManyToManyField(Speaker) #added by Abby
	# secretary = models.ForeignKey(Secretary, on_delete = models.SET_NULL, null = True, related_name = "all_conferences") #added by Abby

	class Meta:
		db_table = "Conference"
			