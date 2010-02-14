from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import logout


users = User.objects.all


def homepage(request):
    if request.user.is_authenticated():
        return redirect('profile_detail')
    return render_to_response('profiles/homepage.html',
                              {'users': users()},
                              RequestContext(request))


def login_as_user(request, username):
    user = authenticate(username=username, password=username)
    if user is not None:
        login(request, user)
        return redirect('profile_detail')
    return redirect('homepage')


def profile_detail(request):
    if not request.user.is_authenticated():
        return redirect('homepage')
    return render_to_response('profiles/profile_detail.html',
                              {'users': users()},
                              RequestContext(request))
