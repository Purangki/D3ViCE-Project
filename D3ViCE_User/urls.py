from django.urls import path
from .import views
from .views import MyPasswordChangeView, MyPasswordResetDoneView

app_name = 'D3ViCE_User'

urlpatterns = [
    path('signUp', views.UserSignUpView.as_view(), name="signUp_view"),
    path('user', views.UserView.as_view(), name="user_view"),
    path('profile', views.UserProfileView.as_view(), name="profile_view"),
    path('change-password/', MyPasswordChangeView.as_view(), name="password-change-view"),
    path('change-password/done/', MyPasswordResetDoneView.as_view(), name="password-change-done-view"),
    path('admin', views.AdminView.as_view(), name="admin_view"),
]