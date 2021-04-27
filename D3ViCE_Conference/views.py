from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect 
from .forms import ConferenceForm
from .models import *
from .models import Conference
from datetime import datetime
from django.contrib.auth.models import auth, User
import uuid		#for the conference code

# Create your views here.
class ConferenceManageView(View):	#conference manage view of conference
	def get(self, request):			#get method for the conference, displays conference details in the template
		qs_conferences = Conference.objects.filter(is_deleted = False, is_created = True, date__gte=datetime.now()).order_by('-date')
		context = {
			'D3ViCE_Conference' : qs_conferences
		}
		return render(request, '10_ManageConferences.html',context)
	def post(self, request):
		if request.method == 'POST':
			if 'btn_create_conference' in request.POST:
				form = ConferenceForm(request.POST or None)
				title = request.POST.get("title_create")
				date = request.POST.get("date_create")
				time = request.POST.get("time_create")
				description = request.POST.get("desc_create")
				form = Conference(title = title,
									date = date,
									time = time,
									description = description,
									code = uuid.uuid1(),
									is_created = True)
				form.save()
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
		return redirect('D3ViCE_Conference:conference_manage_view')

class ConferenceHistoryView(View):
	def get(self, request):
		qs_conferences_created = Conference.objects.filter(is_deleted = False, is_created = True, date__lte=datetime.now()).order_by('-date')
		qs_conferences_joined = Conference.objects.filter(is_deleted = False, is_created = False, date__lte=datetime.now()).order_by('-date')
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
	def get(self, request):
		if request.user.is_authenticated:
			qs_conference_completed = Conference.objects.filter(status = "Completed").order_by('-date')
			qs_conference_ongoing = Conference.objects.filter(status = "Ongoing").order_by('-date')
			qs_conference_upcoming = Conference.objects.filter(status = "Not Started").order_by('-date')
			context = {
				'completed' : qs_conference_completed,
				'ongoing' : qs_conference_ongoing,
				'upcoming' : qs_conference_upcoming,
			}
			return render(request, '6_Dashboard.html', context)
		else:
			return redirect("D3ViCE_Account:login")


		

