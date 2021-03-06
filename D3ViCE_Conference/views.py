import D3ViCE_Conference
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *
from .models import Conference
from D3ViCE_User.models import Profile
from D3ViCE_User.models import *
from datetime import datetime
import uuid		#for the conference code


class ConferenceHistoryView(View):
	def get(self, request):
		current_user = request.user
		qs_conferences_created = current_user.created_conferences.all()
		print(qs_conferences_created)
		qs_conferences_joined = current_user.joined_conferences.all()
		context = {
			'conferences_created' : qs_conferences_created,
			'conferences_joined' : qs_conferences_joined,
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
		current_user = request.user
		qs_conferences = Conference.objects.filter(is_deleted = False).order_by('-date')
		qs_requests = Request.objects.filter(status = 'Pending', target = current_user).order_by('-date')
		context = {
			'conferences' : qs_conferences,
			'requests': qs_requests,
			'current_user': current_user,
		}
		return render(request, '6_Dashboard.html',context)

	def post(self, request):
		if request.method == 'POST':
			if 'btn_create_conference' in request.POST:
				currentUser = Profile.objects.get(id = request.user.id)
				# for validation check if currentUser.is_host == true
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
				# Profile.objects.update(is_host = 1)

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
		
			elif 'btn-accept-request' in request.POST:
				request_id = request.POST.get('request_id')
				request = Request.objects.get(id = request_id)
				request.status = 'Accepted'

				sponsorship = request.sponsorship
				sponsorship.is_accepted = True

				user = request.user
				user.is_sponsor = True

				request.save()
				sponsorship.save()
				user.save()

			elif 'btn-decline-request' in request.POST:
				request_id = request.POST.get('request_id')
				request = Request.objects.get(id = request_id)
				request.status = 'Declined'

				sponsorship = request.sponsorship
				sponsorship.is_accepted = False

				request.save()
				sponsorship.save()
			elif 'btn-search-conference' in request.POST:
				current_user = request.user
				searched = request.POST['search-conference']
				print(searched)
				qs_requests = Request.objects.filter(status = 'Pending', target = current_user).order_by('-date')
				qs_searched = Conference.objects.filter(title__icontains = searched)
				print(qs_searched)
				context = {
					'conferences' : qs_searched,
					'requests': qs_requests,
					'current_user': current_user,
				}
				return render(request, '6_Dashboard.html',context)
		return redirect('D3ViCE_Conference:dashboard_view')
