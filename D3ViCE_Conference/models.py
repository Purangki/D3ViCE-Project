from django.db import models
from datetime import datetime
from D3ViCE_User.models import Profile


class Conference(models.Model):
    code = models.CharField(max_length=50)  # conference code
    title = models.CharField(max_length=150)  # conference title
    date = models.DateField()  # conference start date
    time = models.TimeField()  # conference start time
    end_date = models.DateField(null=True, blank=True)  # conference end date
    end_time = models.TimeField(null=True, blank=True)  # conference end time
    description = models.CharField(max_length=255)  # conference description
    # archives the conference, deleted in the page but not in the db
    is_deleted = models.BooleanField(default=False)
    # added by Abby for the main dashboard
    status = models.CharField(max_length=50, default="Upcoming")
    seats = models.IntegerField()
    type = models.CharField(max_length=255)

    host = models.ForeignKey(Profile, on_delete=models.SET_NULL,
                             related_name="created_conferences", null=True, blank=True)
    participant = models.ManyToManyField(
        Profile, related_name="joined_conferences", blank=True)
    speaker = models.ManyToManyField(
        Profile, related_name="speaker_conferences", blank=True)

    class Meta:
        db_table = "Conference"


class Review(models.Model):
    user = models.ForeignKey(Profile, related_name="event_reviews",
                             blank=True, on_delete=models.SET_NULL, null=True)
    conference = models.ForeignKey(
        Conference, related_name="event_reviews", blank=True, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField()
    # description why mao na ang rating
    feedback = models.CharField(max_length=300)
    date = models.DateField()

    class Meta:
        db_table = "Review"


class Sponsorship(models.Model):
    user = models.ForeignKey(
        Profile, related_name="sponsored_events", on_delete=models.SET_NULL, null=True)
    conference = models.ForeignKey(
        Conference, related_name="sponsors", on_delete=models.SET_NULL, null=True)
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=500)
    company_description = models.CharField(max_length=500)
    reason = models.CharField(max_length=500)
    is_accepted = models.BooleanField(default=False)


class Question(models.Model):
    user = models.ForeignKey(
        Profile, related_name="user_questions", on_delete=models.SET_NULL, null=True)
    conference = models.ForeignKey(
        Conference, related_name="questions", on_delete=models.SET_NULL, null=True)
    about = models.CharField(max_length=1000, null=True, blank=True)
    intended_speaker = models.ForeignKey(
        Profile, related_name="user_speaker", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "Question"
