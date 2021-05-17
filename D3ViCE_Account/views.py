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
class UserLoginView(View):  #view of user when he logs in to the system                    
    def get(self, request): #get method for the template
        return render(request, '5_Login.html')  #render() returns a loaded template

    def post(self, request):                    #post method   
        username = request.POST.get("username") #username 
        password = request.POST.get("password") #user password
        user = auth.authenticate(username = username, password = password)  #using django's builtin authentication system, username & password is checked
        if user is not None:            #if user is not None then
            auth.login(request, user)   #user is logged in on the system
            currentUser = user          #currentUser means that whoever is logged is in that system is the user at present, if this is not set then it is an anonymous user 
            print(str(currentUser.id) + " is logged in")    #prints the current user logged in in the terminal
            context = {                 #context will be used for queries
            'current_user' : currentUser
            }
            return redirect("D3ViCE_Conference:dashboard_view") #redirects the user to the User dashboard
        else:
            return HttpResponse("wrong credentials")    #otherwise if user does not exist and have the wrong credentals then it displays this error

class LogoutView(View):
    def get(self,request):
        logout(request)
        return  redirect("D3ViCE_Account:login")
    def post(self,request):
        logout(request)
        return  redirect("D3ViCE_Account:login")    #if no user is logged in, he cannot go the dashboard even if he manually types the url in the browser



