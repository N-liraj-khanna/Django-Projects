import uuid
from .models import Url
from django.http import HttpResponse
from django.shortcuts import render, redirect

def index(request):
  return render(request, 'index.html')

def create(request):
  if request.method == 'GET':
    return redirect("index")
  else:
    url=request.POST.get('url')
    uid=str(uuid.uuid4())[:5]
    new_url_obj=Url(url=url, uuid=uid)
    new_url_obj.save()
    return HttpResponse(uid)
  
def go(request, pk):
  url_obj = Url.objects.get(uuid=pk)
  url=str(url_obj.url)
  if url[:8]=="https://" or url[:7]=="http://":
    return redirect(url)
  else:
    return redirect("https://"+url)