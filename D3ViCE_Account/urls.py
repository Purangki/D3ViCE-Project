from django.urls import path
from D3ViCE_Account import views

app_name = 'D3ViCE_Account'
urlpatterns = [
	path('login', views.UserLoginView.as_view(), name="login"),
	path('logout', views.LogoutView.as_view(), name="logout"),
] 