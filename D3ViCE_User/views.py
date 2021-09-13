from datetime import date
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import UserForm
from D3ViCE_Account.models import *
from D3ViCE_User.models import *
from D3ViCE_Conference.models import *
from .models import Profile
from django.urls import reverse_lazy
from django.core.mail import EmailMessage #supposed to be for the email authentication, however was put on hold since it is optional
from django.contrib.auth.models import auth, User #builtin django user
from django.contrib.auth.hashers import *
from django.contrib.auth import update_session_auth_hash
class UserSignUpView(View):
	def get(self, request):
		return render(request, '4_SignUp.html')	#user registration

	def post(self, request):	#post method for registraion
		if request.method == 'POST':	
			if 'signUp' in request.POST:
				fname = request.POST.get("fname")
				lname = request.POST.get("lname")
				username = str(fname) + "." + str(lname)
				print(username)
				email = request.POST.get("email")
				password = request.POST.get("pass")
				confirm_password = request.POST.get("confirm_pass")

				if str(password) == str(confirm_password):
					if not Profile.objects.filter(username=username).exists():
						if not Profile.objects.filter(email=email).exists():
							Profile.objects.create_user(first_name=fname,last_name=lname,username=username,email=email,password=password, is_deleted = False, avatar_index = 0)
							user = auth.authenticate(username = username, password = password)  #using django's builtin authentication system, username & password is checked
							if user is not None:            #if user is not None then
								auth.login(request, user)   #user is logged in on the system
								currentUser = user          #currentUser means that whoever is logged is in that system is the user at present, if this is not set then it is an anonymous user 
								print(str(currentUser.id) + " is logged in")    #prints the current user logged in in the terminal
								context = {                 #context will be used for queries
									'current_user' : currentUser
								}
								return redirect("D3ViCE_Conference:dashboard_view") #redirects the user to the User dashboard
							# return redirect('D3ViCE_Conference:dashboard_view')
						else:
							return HttpResponse('email exists')
					else:
						return HttpResponse('Username exists')
				else:
					return HttpResponse("Passwords do not match")

class UserView(View):
	def get(self, request):
		return render(request, '7_EditProfile.html')	#edit profile view (user can see his current details)

class UserProfileView(View):	
	def get(self, request):
		if request.user.is_authenticated:
			qs_user = Profile.objects.filter(is_active=False)
			context = {
				'current_user' : qs_user
			}
			return render(request, '7_EditProfile.html', context)
		else:
			return redirect("D3ViCE_Account:login")

	def post(self, request):
		if request.method == 'POST':
			if 'btn_change_password' in request.POST:
				id_num = request.POST.get("user_id_num")
				current_user = request.user
				current_password = request.POST.get("current_password")
				new_password = request.POST.get("new_password")
				renew_password = request.POST.get("renew_password")
				valid_password = current_user.check_password(current_password)
				if valid_password == True:
					if new_password == renew_password:
						current_user.set_password(new_password)
						update_session_auth_hash(request, current_user)
						current_user.save()
					else:
						return HttpResponse("New passwords don't match")
				else:
					return HttpResponse("Current password does not match your password")
				return redirect("D3ViCE_User:profile_view")
			if 'btn_edit_user' in request.POST:
				id_num = request.POST.get("user_id_num")
				fname = request.POST.get("user-fname")
				lname = request.POST.get("user-lname")
				email = request.POST.get("user-email")
				username = str(fname) + "." + str(lname)
				edit_user = Profile.objects.filter(id = id_num).update(username = username, first_name = fname, last_name = lname, email = email)
				return redirect('D3ViCE_User:profile_view')
			elif 'btn_delete_user' in request.POST:
				id_num = request.POST.get("user_id_num")	
				delete_user = Profile.objects.filter(id = id_num).update(is_active = False)
				return redirect('D3ViCE_Account:login')
class SponsorConferenceView(View):
	def get(self,request,id):
		context = {
			'conference_id' : id
		}
		return render(request, '14_SponsorConference.html', context)

	def post(self, request, id):
		if request.method == 'POST':
			if 'btn_sponsor_conference' in request.POST:
				print(request.POST)
				currentUser = Profile.objects.get(id = request.user.id)
				conference = Conference.objects.get(id = id)
				company_name = request.POST.get('comp_name')
				company_address =  request.POST.get('comp_address')
				company_description =  request.POST.get('comp_description')
				reason = request.POST.get('reason_sponsor')
				target = conference.host
			
				sponsorship = Sponsorship.objects.create(user = currentUser, conference=conference, company_name = company_name, company_address = company_address, company_description = company_description, reason = reason)
				Request.objects.create(user = currentUser, type='Sponsor', description = reason, conference = conference, sponsorship = sponsorship, target = target)

				return redirect('D3ViCE_Conference:dashboard_view')

class AdminDashboardView(View):
	def get(self, request):
		qs_conferences = Conference.objects.filter(is_deleted = False,date__lte=datetime.now()).order_by('-date')
		qs_users = Profile.objects.filter(is_active = False)
		context = {
			'conferences' : qs_conferences,
			'users' : qs_users,
		}
		return render(request, '0_AdminDashboard.html',context)

class AdminUserView(View):
	def get(self, request):
		qs_users = Profile.ojects.filter(is_active = False)
		context = {
			'users' : qs_users,
		}
		return render(request, '0_AdminUser.html', context)		

class AdminConferenceView(View):
	def get(self, request):
		qs_conferences = Conference.objects.filter(is_deleted = False, date__lte = datetime.now().order_by('-date'))
		context = {
			'conferences' : qs_conferences,
		}
		return render(request, '0_AdminConference.html', context)		

class AdminProfileView(View):
	def get(self, request):
		return render(request, '0_AdminProfile.html')				

	