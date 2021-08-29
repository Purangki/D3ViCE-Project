from django.urls import path
from . import views

app_name = 'D3ViCE_Conference'
urlpatterns = [
	# path('manage', views.ConferenceManageView.as_view(), name="conference_manage_view"), #url towards the manage conference (join, create) view of Conference
	path('history', views.ConferenceHistoryView.as_view(), name="conference_history_view"),	#url towards the history view of Conference
	path('dashboard', views.DashboardView.as_view(), name="dashboard_view"),	#url towards the User dashboard view of D3ViCE
	# path('search_conference', views.SearchConferenceView.as_view(), name="search-conference"),
] 
