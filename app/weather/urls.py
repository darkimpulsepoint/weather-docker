from django.urls import path

from weather import views

urlpatterns = [
    path("", views.index),

    path("api/places", views.places, name="places"),
    path("api/weather", views.weather, name="weather")
]