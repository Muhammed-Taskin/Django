from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,"template_app/templates.html")
    
    #render burda template dosyamızı render ediyor.
    #html dosyasınıda gösteriyor diyebiliriz.
#jinja
def weather_view(request):
    weather_dictionary ={
        "Istanbul": "30",
        "Aydın" : "40",
        "İzmir": "20",
        "Ankara": "50",
        "Paris" : [10,20,30,40]
    }
    return render(request,"template_app/weather.html",context= weather_dictionary)
