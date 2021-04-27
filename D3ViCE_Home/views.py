from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect 
from .models import *


# Create your views here.
class HomeView(View):
	def get(self, request):
		return render(request, '1_Home.html')	#homepage

class FeatureView(View):
	def get(self, request):
		return render(request, '2_Feature.html')	#feature page
		
class AboutUsView(View):
	def get(self, request):
		return render(request, '3_AboutUs.html')	#about us page




		

