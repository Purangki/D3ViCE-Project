from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Profile(AbstractUser):
	is_deleted = models.BooleanField(default = False)
	avatar_index = models.IntegerField()

class Host(Profile):
	# user = models.OneToOneField(User, on_delete = models.CASCADE)

	class Meta:
		db_table = "Host"

class Speaker(Profile):
	# user = models.OneToOneField(User, on_delete = models.CASCADE)
	topic = models.CharField(max_length = 150)

	class Meta:
		db_table = "Speaker"

class Secretary(Profile):
	# user = models.OneToOneField(User, on_delete = models.CASCADE)

	class Meta:
		db_table = "Secretary"

class Participant(Profile):
	# user = models.OneToOneField(User, on_delete = models.CASCADE)
	affiliation = models.CharField(max_length = 255, null = True, blank = True)
	display_name = models.CharField(max_length = 255, null = True, blank = True)

	class Meta:
		db_table = "Participant"

class Sponsor(Profile):
	# user = models.OneToOneField(User, on_delete = models.CASCADE)
	sponsor_name = models.CharField(max_length = 255, null = True, blank = True)
	class Meta:
		db_table = "Sponsor"
	