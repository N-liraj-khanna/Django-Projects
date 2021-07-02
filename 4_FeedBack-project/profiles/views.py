from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView

class ProfileView(ListView):
    template_name = 'profiles/list_profiles.html'
    model = UserProfile
    context_object_name = 'profiles'

# def store_profile_picture(file):
#     with open('temp/image.jpg', 'wb+') as img:
#         for chunk in file.chunks():
#             img.write(chunk)

class CreateProfileView(CreateView):
    template_name = 'profiles/create_profile.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/profiles'

# class CreateProfileView(View):  # normal view but inbuilt storage
#     def get(self, request):
#         form=ProfileForm()
#         return render(request, "profiles/create_profile.html",{'form':form})

#     def post(self, request):
#         submitted_form=ProfileForm(request.POST, request.FILES)

#         if submitted_form.is_valid():
#             profiles = UserProfile(image=request.FILES['profile_picture'])
#             profiles.save()
#             return HttpResponseRedirect('/profiles')

#         return render(request, "profiles/create_profile.html",{'form':submitted_form})

# class CreateProfileView(View): # normal method
#     def get(self, request):
#         return render(request, "profiles/create_profile.html")

#     def post(self, request):
#         store_profile_picture(request.FILES['image'])
#         return HttpResponseRedirect('/profiles')
