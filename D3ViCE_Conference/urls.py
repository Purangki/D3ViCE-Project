from django.urls import path
from . import views

app_name = 'D3ViCE_Conference'
urlpatterns = [
	path('manage', views.ConferenceManageView.as_view(), name="conference_manage_view"),
	path('history', views.ConferenceHistoryView.as_view(), name="conference_history_view"),
	path('dashboard', views.DashboardView.as_view(), name="dashboard_view"),
] 
