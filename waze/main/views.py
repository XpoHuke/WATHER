from django.shortcuts import render
import requests
from .models import City
from . forms import CityForm

def index(request):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=1940ecde4e08fb7f31ee1a826759b89f"
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm
    cities = City.objects.all()
    all_c = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res['weather'][0]['icon']
        }
        all_c.append(info)
    context = {
        'info': all_c,
        'form': form
    }
    return render(request, 'index.html', context)
