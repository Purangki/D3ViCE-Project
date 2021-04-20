from django.urls import path
from . import views

app_name = 'D3ViCE_Home'
urlpatterns = [
	path('home', views.HomeView.as_view(), name="1_Home"),
	path('feature', views.FeatureView.as_view(), name="2_Feature"),
	path('aboutUs', views.AboutUsView.as_view(), name="3_AboutUs"),
] 
