from django.urls import path
from . import views

app_name = 'D3ViCE_Home'
urlpatterns = [
	path('home', views.HomeView.as_view(), name="1_Home"),	#url towards the home views.py
	path('feature', views.FeatureView.as_view(), name="2_Feature"),	#url towards the feature views.py
	path('aboutUs', views.AboutUsView.as_view(), name="3_AboutUs"),	#url towards the about us views.py
] 
