"""D3ViCE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), #this is a path for the admin page
    path('D3ViCE_Account/', include('D3ViCE_Account.urls', namespace='account')), #this is a path for the account urls
    path('D3ViCE_Conference/', include('D3ViCE_Conference.urls', namespace='conference')), #this is a path for the conference urls
    path('D3ViCE_Home/', include('D3ViCE_Home.urls', namespace='home')), #this is a path for the home urls
    path('D3ViCE_User/', include('D3ViCE_User.urls', namespace='user')), #this is a path for the user urls
    path('D3ViCE_Unity/', include('D3ViCE_Unity.urls', namespace='unity')), #this is a path for the unity urls
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #this is for the media files
