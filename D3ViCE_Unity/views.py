#
# Authors: MCiVillondo
# Descrition: D3ViCE_Unity.views contains all methods used in unity to get data from python server.
#
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import auth, AbstractUser

from .forms import *
from D3ViCE_User.models import Profile
# Create your views here.

@csrf_exempt
def login_user(request, username=None):
    user_data = get_object_or_404(auth, username=username)
    form = UserLogin(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user_name =  form.cleaned_data["username"]
            user_password = form.cleaned_data["password"]
            user = auth.authenticate(username = user_name, password = user_password)
            if user is not None:
                user_username = user_data.username
                user_firstname = user_data.firstName
                user_lastname = user_data.lastName
                user_email = user_data.email
                user_avatarindex = user_data.avatar_index
                return JsonResponse({'success': True, 'user': user_username,'firstname': user_firstname,'lastname': user_lastname,'email': user_email,'avatar_index': user_avatarindex})
            else:
                return JsonResponse({'success': False, 'errors': 'Invalid Password'})
        else:
            form.errors.as_json()
            return JsonResponse({'success': False, 'errors':[(k,v[0]) for k,v in form.errors.items()]})

@csrf_exempt
def update_avatar(request):
    if request.method == "POST":
        form = UserUpdateAvatar(request.POST or None)
        if form.is_valid():
            user_username = request.POST.get("username")
            user_newavatar = request.POST.get("index")

            form = Profile.objects.filter(username = user_username).update(avatar_index = user_newavatar)
            return JsonResponse({'success': True})
        else:
            form.error.as_json()
            return JsonResponse({'success': False, 'errors':[(k,v[0]) for k,v in form.errors.items()]})

@csrf_exempt
def join_conference(request, code=None):
    conference_data = get_object_or_404(Conference, code=code)
    form = UserJoinConference(request.POST or None)
    if request.method == "POST":
        conference_code = conference_data.code
        user_code = form.cleaned_data["code"]

        if conference_code == user_code:
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': 'Invalid Code'})
    else: 
        form.error.as_json()
        return JsonResponse({'success': False, 'errors':[(k,v[0]) for k,v in form.errors.items()]})

@csrf_exempt
def register_participant(request):
    if request.method == "POST":
        form = RegisterParticipant(request.POST or None)

        if form.is_valid():
            user_username = request.POST.get("username")
            user_displayname = request.POST.get("displayname")
            user_affliation = request.POST.get("affiliation")

            participants = Participant.object.all()
            count = 0

            for participant in participants:
                if participant.username == user_username:
                    ++count

            users = Profile.object.all()

            for user in users:
                if user.username == user_username:
                    user_id = user.id

            if count == 0:
                form = Participant(id = user_id,  display_name = user_displayname, affiliation = user_affliation)
                form.save()
            else:
                form = Participant.objects.filter(id = user_id).update(display_name = user_displayname, affiliation = user_affliation)

            return JsonResponse({'success': True})
        else:
            form.error.as_json()
            return JsonResponse({'success': False, 'errors':[(k,v[0]) for k,v in form.errors.items()]})

