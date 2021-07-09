from D3ViCE_Conference.models import Conference
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Profile(AbstractUser):
	is_deleted = models.BooleanField(default = False)
	avatar_index = models.IntegerField(null = True, blank = True)
	type_of_plan = models.CharField(max_length = 255, null = True, blank = True) #which plan each user is availing

class Organizer(Profile):

	class Meta:
		db_table = "Organizer"

class Speaker(Profile):
	topic = models.CharField(max_length = 150)

	class Meta:
		db_table = "Speaker"

class Secretary(Profile):

	class Meta:
		db_table = "Secretary"

class Participant(Profile):
	affiliation = models.CharField(max_length = 255, null = True, blank = True)
	display_name = models.CharField(max_length = 255, null = True, blank = True)

	class Meta:
		db_table = "Participant"

class Sponsor(Profile):
	sponsor_name = models.CharField(max_length = 255, null = True, blank = True)
	class Meta:
		db_table = "Sponsor"

# additional model





	