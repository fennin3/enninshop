from django.urls import path
from .views import add_to_cart, remove_from_cart, OrderSummaryView, CheckoutView



urlpatterns = [
    path('order-summary/', OrderSummaryView.as_view(), name='order_summary'),
    path('add-to-cart/<slug>', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<slug>', remove_from_cart, name='remove_from_cart'),
     path('checkout/', CheckoutView.as_view(), name='checkout_home'),

   
    # path('/', OrderSummaryView.as_view(), name='product_detail')
    
    
]
