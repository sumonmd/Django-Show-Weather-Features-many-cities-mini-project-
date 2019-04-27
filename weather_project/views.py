from django.http import HttpRequest
from django.shortcuts import render

from weather_project import weather_service


def index(request: HttpRequest):
    cities =['Rajshahi', 'Khulna', 'Dhaka', 'London', 'Christchurch']
    return render(request, 'index.html', context={
        'weather_data': [weather_service.get_weather(city) for city in cities]
    })
