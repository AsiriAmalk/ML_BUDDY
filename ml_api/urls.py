from django.urls import path

from . import views

# always end our routs with forward slash

urlpatterns = [path("hello/", views.say_hello)]
