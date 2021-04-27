from django.urls import path
from .import views
from .views import MyPasswordChangeView, MyPasswordResetDoneView

app_name = 'D3ViCE_User'

urlpatterns = [
    path('signUp', views.UserSignUpView.as_view(), name="signUp_view"), #url towards the signUp views.py
    path('user', views.UserView.as_view(), name="user_view"),   #url towards the user (edit profile) views.py 
    path('profile', views.UserProfileView.as_view(), name="profile_view"),  #url towards the User Profile views.py
    path('change-password/', MyPasswordChangeView.as_view(), name="password-change-view"), #url towards the change password views.py
    path('change-password/done/', MyPasswordResetDoneView.as_view(), name="password-change-done-view"), #url towards the password reset views.py
    path('admin', views.AdminView.as_view(), name="admin_view"), #url towards the admin views.py
]