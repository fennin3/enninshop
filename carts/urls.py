from django.urls import path
from .views import add_to_cart, remove_from_cart, OrderSummaryView, CheckoutView, edit_profile, subquantity



urlpatterns = [
    path('order-summary/', OrderSummaryView.as_view(), name='order_summary'),
    path('add-to-cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/order/<int:id>/', CheckoutView, name='checkout_home'),
    path('checkout/profile-edit/<int:id>/', edit_profile, name='profile_edit'),
    path('add-quantity/cart/<int:id>/', subquantity, name="subproduct")
]
