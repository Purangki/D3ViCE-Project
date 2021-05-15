from django.urls import path
from .views import *
from . import views

#path arranged alphabetically by name
app_name = 'D3ViCE_Unity'

urlpatterns=[
    path('unity/login/<slug:username>/', login_user, name="login"),
    path('unity/update_avatar/', update_avatar, name="update"),
    path('unity/join/<slug:code>/', join_conference, name="join"),
    path('unity/participant/', register_participant, name="participant"),
]