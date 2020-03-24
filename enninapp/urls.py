from django.urls import path
from .views import HomeView, ItemDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='enninapp_home'),
 	path('product-detail/<slug>/', ItemDetailView.as_view(), name='product_detail')       
]
