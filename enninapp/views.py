from django import urls
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Product, Category, Subscriber, Brand
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .filters import ProductFilter

class ItemDetailView(DetailView):
	model = Product
	template_name = 'enninapp/product-detail.html'


def home(request):
    products = Product.objects.all()
    category = Category.objects.all()
    featured = Product.objects.filter(is_featured=True)
    brands = Brand.objects.all()


    context = {
        'products': products,
        'category': category,
        'featured': featured,
        'brands':brands
    }
    return render(request, 'enninapp/index.html', context)



def searchresult(request):
    if request.method == "POST":
        query = request.POST.get('search', None)
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    context = {
    	'products': products,
		'query':query
    }
    print(query)
    return render(request, 'enninapp/search_results.html', context)
    



def subscribe(request):
    if request.method == "POST":
        email = request.POST.get('email')

        Subscriber.objects.create(email=email)
        return redirect('enninapp_home')


def cat_detail(request, id):
    cat = Category.objects.get(id=id)

    context = {
        'cat':cat,
    }

    return render(request, 'enninapp/product.html', context)

def prod_detail(request, id):
    prod = Product.objects.get(id=id)
    related_prod = Product.objects.exclude(id=id)
    context = {
        'prod':prod,
        'related_prod':related_prod,
    }
    
    return render(request, 'enninapp/product-detail.html', context)


def brand_page(request, id):
    brand = Brand.objects.get(id=id)

    context = {
        'brand':brand
    }
    return render(request, 'enninapp/brand.html', context)


def contact_us(request):
    return render(request, 'enninapp/contact.html')


