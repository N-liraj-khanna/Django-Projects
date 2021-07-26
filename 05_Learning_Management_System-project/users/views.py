from django.shortcuts import render
from .forms import UserForm,UserProfileForm
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html',{})

def registration(request):
    registered=False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and user_profile_form.is_valid():
            user=user_form.save()
            user.save()

            profile=user_profile_form.save(commit=False)
            profile.user=user
            profile.save()

            registered = True
        else:
            print(user_profile_form.errors, user_form.errors)
    else:
        user_form=UserForm()
        user_profile_form=UserProfileForm()
    
    return render(request, 'registration.html', {
        'registered': registered,
        'user_form': user_form,
        'user_profile_form': user_profile_form,
    })

def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('ACCOUNT DEACTIVATED')
        else:
            return HttpResponse('Check the username and password!!')
    else:
        return render(request, 'login.html')
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))