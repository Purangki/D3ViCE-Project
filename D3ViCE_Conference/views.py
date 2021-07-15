from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect 
from .forms import ConferenceForm
from .models import *
from .models import Conference
from D3ViCE_User.models import Profile
from datetime import datetime
from django.contrib.auth.models import auth, User
from django.contrib.auth import get_user_model
import uuid		#for the conference code

# Create your views here.
# class ConferenceManageView(View):	#conference manage view of conference
# 	def get(self, request):			#get method for the conference, displays conference details in the template
# 		qs_conferences = Conference.objects.filter(is_deleted = False, date__gte=datetime.now()).order_by('-date')
# 		context = {
# 			'D3ViCE_Conference' : qs_conferences
# 		}
# 		return render(request, '10_ManageConferences.html',context)
# 	def post(self, request):
# 		if request.method == 'POST':
# 			if 'btn_create_conference' in request.POST:
# 				print("button click")
# 				form = ConferenceForm(request.POST or None)
# 				title = request.POST.get("title_create")
# 				date = request.POST.get("date_create")
# 				time = request.POST.get("time_create")
# 				description = request.POST.get("desc_create")
# 				form = Conference(title = title,
# 									date = date,
# 									time = time,
# 									description = description,
# 									code = uuid.uuid1())
# 				form.save()
# 			elif 'btn_edit_conference' in request.POST:
# 				id_num = request.POST.get("conference_id_num")
# 				title = request.POST.get("title_edit")
# 				date = request.POST.get("date_edit")
# 				time = request.POST.get("time_edit")
# 				description = request.POST.get("desc_edit")
# 				edit_conference = Conference.objects.filter(id = id_num).update(title = title, date = date, time = time, description = description)
# 			elif 'btn_delete_conference' in request.POST:
# 				id_num = request.POST.get("conference_id_num")	
# 				delete_conference = Conference.objects.filter(id = id_num).update(is_deleted = True)
# 		return redirect('D3ViCE_Conference:conference_manage_view')

class ConferenceHistoryView(View):
	def get(self, request):
		qs_conferences_created = Conference.objects.filter(is_deleted = False,date__lte=datetime.now()).order_by('-date')
		qs_conferences_joined = Conference.objects.filter(is_deleted = False,date__lte=datetime.now()).order_by('-date')
		context = {
			'conferences_created' : qs_conferences_created,
			'conferences_joined' : qs_conferences_joined  
		}
		return render(request, '11_ViewHistory.html',context)
	def post(self, request):
		if request.method == 'POST':
			if 'btn_delete_conference' in request.POST:
				id_num = request.POST.get("conference_id_num")	
				delete_conference = Conference.objects.filter(id = id_num).update(is_deleted = True)
		return redirect('D3ViCE_Conference:conference_history_view')

class DashboardView(View):
	def get(self, request):			#get method for the conference, displays conference details in the template
		qs_conferences = Conference.objects.filter(is_deleted = False, date__gte=datetime.now()).order_by('-date')
		context = {
			'D3ViCE_Conference' : qs_conferences
		}
		return render(request, '6_Dashboard.html',context)
	def post(self, request):
		if request.method == 'POST':

			if 'btn_create_conference' in request.POST:
				User = get_user_model()
				currentUser = Profile.objects.get(id = request.user.id)
				print(request.user)
				print(currentUser.id)

				print("button click")

				title = request.POST.get("title_create")
				type = request.POST.get("select_type")
				start_date = request.POST.get("date_create")
				start_time = request.POST.get("time_create")
				end_date = request.POST.get("date_end")
				end_time = request.POST.get("time_end")
				description = request.POST.get("desc_create")
				seats = request.POST.get("num_seats")

				Conference.objects.create(title = title,
									date = start_date,
									time = start_time,
									end_date = end_date,
									end_time = end_time,
									description = description,
									seats = seats,
									type = type,
									host = currentUser,
									code = uuid.uuid1())

			elif 'btn_edit_conference' in request.POST:
				id_num = request.POST.get("conference_id_num")
				title = request.POST.get("title_edit")
				date = request.POST.get("date_edit")
				time = request.POST.get("time_edit")
				description = request.POST.get("desc_edit")
				edit_conference = Conference.objects.filter(id = id_num).update(title = title, date = date, time = time, description = description)
			
			elif 'btn_delete_conference' in request.POST:
				id_num = request.POST.get("conference_id_num")	
				delete_conference = Conference.objects.filter(id = id_num).update(is_deleted = True)
		
		return redirect('D3ViCE_Conference:dashboard_view')

		

