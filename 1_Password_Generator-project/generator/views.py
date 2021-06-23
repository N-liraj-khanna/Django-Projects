from django.shortcuts import render
from django.http import HttpResponse
import string
import random

# Create your views here.

def home(req):
    return render(req, 'generator/home.html')

def about(req):
    return render(req, 'generator/about.html')

def password(req):

    length = int(req.GET.get('length', 12))
    password = string.ascii_lowercase

    if req.GET.get('upper'):
        password += string.ascii_uppercase
    if req.GET.get('num'):
        password += string.digits
    if req.GET.get('special'):
        password += "~`!@#$%^&*()-+={[}]|:\;\"'<,>.?/"

    random_password = "".join(random.sample(list(password), length))

    return render(req, 'generator/password.html', {'password': random_password})