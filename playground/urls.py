from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

# urlconf conf module goes for url configuration
urlpatterns = [path("hello/", views.say_hello)]
