from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import auth, User #builtin django user

from .models import *

# Create your views here.
class UserLoginView(View):
    def get(self, request):
        return render(request, '5_Login.html')

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            currentUser = user
            print(str(currentUser.id) + " is logged in")
            context = {
            'current_user' : currentUser
            }
            return redirect("D3ViCE_Conference:dashboard_view")
        else:
            return HttpResponse("wrong credentials")

class LogoutView(View):
    def get(self,request):
        logout(request)
        return  redirect("D3ViCE_Account:login")
    def post(self,request):
        logout(request)
        return  redirect("D3ViCE_Account:login")



