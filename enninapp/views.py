from django import urls
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Product, Category, Subscriber, Brand
from carts.models import Order
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .filters import ProductFilter
from django.conf import settings
from enninapp.random_gen import get_random_string
from django.utils import timezone

class ItemDetailView(DetailView):
	model = Product
	template_name = 'enninapp/product-detail.html'


def home(request):
    products = Product.objects.all()
    category = Category.objects.all()
    featured = Product.objects.filter(is_featured=True)
    brands = Brand.objects.all()
    try:
        latest = Product.objects.all()[:6]
    except Exception:
        latest = Product.objects.all()


    context = {
        'products': products,
        'category': category,
        'featured': featured,
        'brands':brands,
        'latest':latest
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

def featured_product(request):
    featured = Product.objects.filter(is_featured=True)
    context = {
        'featured':featured
    }
    return render(request, 'enninapp/featured.html', context)

# def make_payment(request, id):
#     ref = get_random_string(20)
#     try:
#         order = Order.objects.get(id=id)
#         context = {
#             'key':'FLWPUBK_TEST-070399e72975cc67ce8492c0b014cd0d-X',
#             'objects': order,
#             'ref':ref
#         }
#         return render(request, 'enninapp/payment.html', context)
#     except Exception as e:
#         print(e)
#         return redirect('/')


def success(request, id):
    order = Order.objects.get(id=id)
    order.ordered = True
    for item in order.items.all():
        item.ordered = True
        item.save()
    order.ordered_date = timezone.now()
    order.save()
    return render(request, 'enninapp/success.html')