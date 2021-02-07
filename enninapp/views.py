from django import urls
from django.db.models import query
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Product, Category, Subscriber, Brand
from carts.models import Order, OrderedItem
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .filters import ProductFilter
from django.conf import settings
from enninapp.random_gen import get_random_string
from django.utils import timezone
from django.core.paginator import Paginator

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
    query = ""
    if request.method == "POST":
        query = request.POST.get('search', None)
    if query:
        prod = Product.objects.filter(name__icontains=query)
        products = Paginator(prod, 20)

    else:
        prod = Product.objects.all()
        products = Paginator(prod, 20)
    
    page_number = request.GET.get('page')
    page_obj = products.get_page(page_number)
    
    context = {
    	'products': page_obj,
		'query':query
    }
    
    return render(request, 'enninapp/search_results.html', context)


def shop(request):
    prod = Product.objects.all()
    products = Paginator(prod, 20)
    page_number = request.GET.get('page')
    page_obj = products.get_page(page_number)
    
    context = {
    	'products': page_obj,
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
    cat_products = Paginator(cat.products.all(), 20)
    page_number = request.GET.get('page')
    page_obj = cat_products.get_page(page_number)

    context = {
        'cat':page_obj,
        'category_':cat
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


def success(request, id):
    order = Order.objects.get(id=id)
    order.ordered = True
    for item in order.items.all():
        item.ordered = True
        item.save()
    order.ordered_date = timezone.now()
    order.save()

    ordered_item = OrderedItem.objects.create(
        user = order.user,
        ordered_date = timezone.now(),
        address = order.user.profile.address,
        phonenumber = order.user.profile.phone_number,
    )
    ordered_item.save()
    for i in order.items.all():
        ordered_item.items.add(i)
    return render(request, 'enninapp/success.html')