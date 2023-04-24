from django.http import HttpResponse

from django.shortcuts import render
import json
from .utils import get_places, get_weather
# Create your views here.


def index(request):
    return render(request, "index.html")


def places(request):
    places_list = get_places(request.GET.get("city", ""))
    json_object = json.dumps({"places": places_list})
    return HttpResponse(json_object)


def weather(request):
    url = request.GET.get("url")
    weather = get_weather(url)
    return HttpResponse(json.dumps(weather))
