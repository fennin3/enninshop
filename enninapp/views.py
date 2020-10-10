from django import urls
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Product
from .models import Category
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect



class HomeView(ListView):
	model = Product
	template_name = 'enninapp/index.html'





class ItemDetailView(DetailView):
	model = Product
	template_name = 'enninapp/product.html'











