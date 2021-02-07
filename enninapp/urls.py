from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='enninapp_home'),
    path('search-products/', views.searchresult, name="search"),
    path('shop/', views.shop, name="shop"),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('category/<int:id>/', views.cat_detail, name="cat_detail"),
    path('product-detail/<int:id>/', views.prod_detail, name='prod_detail'),
    path('brand/<int:id>/', views.brand_page, name='brand'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('featured-products/', views.featured_product, name="featured"),
    path('payment-successful/<int:id>/', views.success, name="success")
]
