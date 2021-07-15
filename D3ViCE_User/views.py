from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import UserForm
from D3ViCE_Account.models import *
from D3ViCE_User.models import *
from .models import Profile
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django.core.mail import EmailMessage #supposed to be for the email authentication, however was put on hold since it is optional

class MyPasswordChangeView(PasswordChangeView):
	template_name = '8_ChangePassword.html'	#changing password template
	success_url = reverse_lazy('D3ViCE_User:password-change-done-view')	#password successful

class MyPasswordResetDoneView(PasswordResetDoneView):
	template_name = '9_SuccessfulChangePass.html'	#password successful template

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
							user = Profile.objects.create_user(first_name=fname,last_name=lname,username=username,email=email,password=password, is_deleted = False, avatar_index = 0)
							return redirect('D3ViCE_Conference:dashboard_view')
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
				
				return redirect('D3ViCE_User:password-change-view')
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

class AdminView(View):	#admin dashboard
	def get(self, request):
		return render(request, '0_AdminDashboard.html')

class SponsorConferenceView(View):
	def get(self,request):
		return render(request, '14_SponsorConference.html')

	def post(self, request):
		if request.method == 'POST':
			if 'btn_sponsor_conference' in request.POST:

				# currentUser = request.user.id
				# company_name = request.POST.comp_name
				# company_address =  request.POST.comp_address
				# company_address =  request.POST.comp_description
				# reason = request.POST.reason_sponsor


				return render('D3ViCE_User:sponsor_conference_view')

	