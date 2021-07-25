import requests
from .models import Weather 
from .forms import Form
from django.shortcuts import render

API_KEY="49de35b807b87c29e2319f101ab892a6"

URL="https://api.openweathermap.org/data/2.5/weather"
params={'appid': API_KEY,'units': 'metric'}

def index(request):
  error=False
  if request.method == 'POST':
    city=request.POST.get('city').title()
    data_exist = Weather.objects.filter(city=city)
    for data in data_exist:
      data.delete()
    params['q']=city
    response = requests.get(URL, params=params)
    data=response.json()
    try:
      temp=data['main']['temp']
      data=data['weather'][0]
      new_data = Weather(
        icon=data['icon'],
        description=data['description'],
        temperature=temp,
        city=city,
      )
      new_data.save()
    except KeyError:
      error=True
    
  form=Form()
  weather_data = Weather.objects.all().order_by('-id')
  return render(request, 'weather/weather.html', context={'weather_data': weather_data, 'form':form, 'error': error})