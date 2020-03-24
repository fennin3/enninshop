from django.urls import path
from . import views


urlpatterns = [
    path('', views.Register, name='enninapp_home'),
    
]