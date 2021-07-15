from django.urls import path
from .views import *
from . import views

#path arranged alphabetically by name
app_name = 'D3ViCE_Unity'
urlpatterns=[
    #path('unity/login/<slug:username>/', login_user, name="unitylogin"),
    path('unity/login/', login_user, name="unitylogin"),
    path('unity/update_avatar/', update_avatar, name="unityupdate"),
    path('unity/join/<slug:code>/', join_conference, name="unityjoin"),
    path('unity/participant/', register_participant, name="unityparticipant"),
    path('webgl', views.WebglView.as_view(), name="12_Webgl"),	#url towards the webgl views.py
]