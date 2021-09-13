#
# Authors: MCiVillondo
# Descrition: D3ViCE_Unity.views contains all functions and class used in unity to get data through the django server.
#
import re
from sys import displayhook
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import auth, User  # builtin django user

from .forms import *
from D3ViCE_User.models import Profile
from D3ViCE_Conference.models import Conference, Question

from django.shortcuts import render
from django.views.generic import View
# Create your views here.

# D3ViCE_Unity.login_user function is responsible for the user login in unity. Unity sends a WWWForm containing the user credentials, meanwhile django recieves and autheticates the credentials through this function.


@csrf_exempt
def login_user(request):
    print("D3ViCE_Unity: user from unity is attempting to login")
    user_name = request.POST.get("username")
    user_data = get_object_or_404(Profile, username=user_name)

    if request.method == "POST":
        print("Request Method: POST")
        user_password = request.POST.get("password")
        print("Username Recieved")
        print("Password Recieved")
        user = auth.authenticate(username=user_name, password=user_password)

        if user is not None:
            print("Login Status: Sucessful")
            user_idNumber = user_data.id
            user_username = user_data.username
            user_firstname = user_data.first_name
            user_lastname = user_data.last_name
            user_email = user_data.email
            user_avatarindex = user_data.avatar_index

            return JsonResponse({'success': True, 'id': user_idNumber, 'user': user_username, 'firstname': user_firstname, 'lastname': user_lastname, 'email': user_email, 'avatar_index': user_avatarindex})
        else:
            print("Login Status: Failure")
            return JsonResponse({'success': False, 'errors': 'Invalid Password'})


# D3ViCE_Unity.update_avatar function is responsible for the updating the user's preferred avatar.
@csrf_exempt
def update_avatar(request):
    print("D3ViCE_Unity: user from unity is attempting to update avatar index")
    if request.method == "POST":
        print("Request Method: POST")
        # form = UserUpdateAvatar(request.POST or None)
        # if form.is_valid():
        user_username = request.POST.get("username")
        print(user_username)
        user_newavatar = request.POST.get("index")
        print(user_newavatar)

        Profile.objects.filter(username=user_username).update(
            avatar_index=user_newavatar)
        print("Update Avatar Index: Sucessful")
        return JsonResponse({'success': True})
        # else:
        #     form.error.as_json()
        #     print("Form: !Valid")
        #     return JsonResponse({'success': False, 'errors':[(k,v[0]) for k,v in form.errors.items()]})

# D3ViCE_Unity.join_conference function is responsible for the vertifying if a user can join a conference through a conference code.


@csrf_exempt
def join_conference(request, code=None):
    print("D3ViCE_Unity: user from unity is attempting to join a conference")
    conference_data = get_object_or_404(Conference, code=code)
    form = UserJoinConference(request.POST or None)
    if request.method == "POST":
        print("Request Method: POST")
        conference_code = conference_data.code
        conference_name = conference_data.title

        user_code = request.POST.get("code")
        print(user_code)

        if conference_code == user_code:
            print("Join Conference: Sucessful")
            return JsonResponse({'success': True, 'conference_title': conference_name})
        else:
            print("Join Conference: Failure")
            return JsonResponse({'success': False, 'errors': 'Invalid Code'})
    else:
        form.error.as_json()
        print("Request Method: !POST")
        return JsonResponse({'success': False, 'errors': [(k, v[0]) for k, v in form.errors.items()]})

# D3ViCE_Unity.register_participant function is responsible for the participant registration to the conference.


@csrf_exempt
def register_participant(request):
    print("D3ViCE_Unity: user from unity is attempting to register to a conference")
    user_name = request.POST.get("username")
    conference_code = request.POST.get("conference_code")
    user_data = get_object_or_404(Profile, username=user_name)
    conference_data = get_object_or_404(Conference, code=conference_code)

    if request.method == "POST":
        print("Request Method: POST")

        print(user_name)
        print(conference_code)

        user_idnumber = user_data.id
        user_displayname = request.POST.get("displayname")
        print(user_displayname)
        user_affliation = request.POST.get("affiliation")
        print(user_affliation)

        participant_resgister = Profile.objects.filter(id=user_idnumber).update(
            affiliation=user_affliation, display_name=user_displayname)

        user_isHost = user_data.is_host
        user_isSponsor = user_data.is_sponsor
        user_isSpeaker = user_data.is_speaker

        conference = Conference.object.filter(code=conference_code)
        conference.participant.add(user_idnumber)
        participants_count = Conference.participant.all().count()

        print("Participant Registration: Sucessful")
        return JsonResponse({'success': True, 'is_host':  user_isHost, 'is_speaker': user_isSpeaker, 'is_sponsor': user_isSponsor, 'number_participants': participants_count})
    """ else:
        print("Form: !Valid")
        form.error.as_json()
        return JsonResponse({'success': False, 'errors': [(k, v[0]) for k, v in form.errors.items()]}) """


@csrf_exempt
def unity_updateprofile(request):
    print("D3ViCE_Unity: user from unity is attempting to update their profile information")
    form = UpdateUserProfile(request.POST or None)
    if request.method == "POST":
        print("Request Method: POST")
        user_username = request.POST.get("username")
        print(user_username)
        user_newdisplayname = request.POST.get("display_name")
        print(user_newdisplayname)
        user_newaffiliation = request.POST.get("affliation")
        print(user_newaffiliation)
        user_newemail = request.POST.get("email")
        print(user_newaffiliation)

        update_profile = Profile.objects.filter(username=user_username).update(
            display_name=user_newdisplayname, affiliation=user_newaffiliation, email=user_newemail)
        print("Update User Profile: Sucessful")
        return JsonResponse({'success': True})
    else:
        print("Form: !Valid")
        form.error.as_json()
        return JsonResponse({'success': False, 'errors': [(k, v[0]) for k, v in form.errors.items()]})


def unity_addquestion(request):
    print("D3ViCE_Unity: user from unity is attempting to send a question")
    form = AddQuestion(request.POST or None)
    if request.method == "POST":
        print("Request Method: POST")

        question_sender = request.POST.get("userID")
        print(question_sender)

        question_conferencecode = request.POST.get("conferenceCode")
        question_conference = Conference.object.filter(
            code=question_conferencecode)
        question_conferenceid = question_conference.id
        print(question_conferencecode)
        print(question_conferenceid)

        question_about = request.POST.get("about")
        print(question_about)

        question_reciever_username = request.POST.get("speaker")
        question_reciever_id = Profile.objects.filter(
            username=question_reciever_username)
        print(question_reciever_username)
        print(question_reciever_id)

        add_question = Question.ojects.create(
            user=question_sender, conference=question_conferenceid, about=question_about, intended_speaker=question_reciever_id)
        print(add_question)

        print("Question Added: Sucessful")
        return JsonResponse({'success': True})

    else:
        print("Form: !Valid")
        form.error.as_json()
        return JsonResponse({'success': False, 'errors': [(k, v[0]) for k, v in form.errors.items()]})


def unity_getquestions(request):
    print("D3ViCE_Unity: user from unity is attempting to get a questions for question bank")
    if request.method == "POST":
        print("Request Method: POST")

        question_conferencecode = request.POST.get("conferenceCode")
        question_conference = Conference.object.filter(
            code=question_conferencecode)
        question_conferenceid = question_conference.id
        print(question_conferencecode)
        print(question_conferenceid)

        questions = Question.objects.all()

        print("Question Gotten: Sucessful")
        return JsonResponse({'success': True, 'question': questions})


class WebglView(View):
    def get(self, request):
        return render(request, '12_Webgl.html')  # Webgl
