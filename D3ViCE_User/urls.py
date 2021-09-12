from django.urls import path
from .import views

app_name = 'D3ViCE_User'

urlpatterns = [
    path('signUp', views.UserSignUpView.as_view(), name="signUp_view"), #url towards the signUp views.py
    path('user', views.UserView.as_view(), name="user_view"),   #url towards the user (edit profile) views.py 
    path('profile', views.UserProfileView.as_view(), name="profile_view"),  #url towards the User Profile views.py
    path('sponsor/<int:id>', views.SponsorConferenceView.as_view(), name = "sponsor_conference_view")
]