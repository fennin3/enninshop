from django.apps import AppConfig
from django.shortcuts import render_to_response


class EnninappConfig(AppConfig):
    name = 'enninapp'


def home(resquest):
	return render_to_response("index.html")