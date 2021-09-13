from django.urls import path
from . import views

app_name = 'D3ViCE_Conference'
urlpatterns = [
	path('history', views.ConferenceHistoryView.as_view(), name="conference_history_view"),	#url towards the history view of Conference
	path('dashboard', views.DashboardView.as_view(), name="dashboard_view"),	#url towards the User dashboard view of D3ViCE
] 
