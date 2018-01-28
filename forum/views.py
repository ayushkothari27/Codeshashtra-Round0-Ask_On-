from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile


def login(request):
    if request.user.is_authenticated:
            return render(request, 'forum/feed.html', {})
    else:
        if request.method == 'POST':
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth_login(request, user)
                    return render(request, 'forum/feed.html', {})
                else:
                    error = 'Your account is disabled.'
                    return render(request, 'forum/login.html', {'error': error})
            else:
                error = 'Incorrect Username or Password'
                return render(request, 'forum/login.html', {'error': error})
        else:
            return render(request, 'forum/login.html', {})


def logout(request):
    auth_logout(request)
    return redirect(reverse('login'))


@login_required(login_url='/login/')
def profile(request, idx):
    client = get_object_or_404(UserProfile, pk=idx)

    return render(request, 'forum/user_profile.html', {'client': client})



