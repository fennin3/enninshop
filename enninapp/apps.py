from django.apps import AppConfig
from django.shortcuts import render


class EnninappConfig(AppConfig):
    name = 'enninapp'


def home(request):
	return render(request, "index.html")