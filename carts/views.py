from users.models import Profile
from users.forms import ProfileAddressForm
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from enninapp.models import Product
from .models import Order, OrderItem, OrderedItem
from django.utils import timezone
from django.views.generic import View
from enninapp.random_gen import get_random_string
from django.conf import settings
	

 
class OrderSummaryView(LoginRequiredMixin, View):
	def get(self, *args, **kwargs):
		try:
			order = Order.objects.get(user=self.request.user, ordered=False)
			context = {
				'objects': order
			}
			return render(self.request, 'enninapp/cart.html', context)
		except ObjectDoesNotExist:
			messages.info(self.request, "You do not have an active order")
			return redirect("enninapp_home")
		




@login_required
def add_to_cart(request, id):
	item = get_object_or_404(Product, id=id)
	order_item, created = OrderItem.objects.get_or_create(
		item=item,
		user=request.user,
		ordered=False
		)
	order_qs = Order.objects.filter(user=request.user, ordered=False)
	if order_qs.exists():
		order = order_qs[0]
		#check if order item is in the order
		if order.items.filter(item__id=item.id).exists():
			order_item.quantity += 1
			order_item.save()
			messages.info(request, "This item quantity was update.")
			# return redirect('prod_detail', id=id)
			return redirect(request.META['HTTP_REFERER'])
		else:
			order.items.add(order_item)
			messages.info(request, "This item was added to your cart.")
			# return redirect('prod_detail', id=id)
			return redirect(request.META['HTTP_REFERER'])

	else:
		ordered_date = timezone.now()
		order = Order.objects.create(user=request.user, ordered_date=ordered_date)
		order.save()
		order.items.add(order_item)
		messages.info(request, "This item was added to your cart.")

		# return redirect('prod_detail', id=id)
		return redirect(request.META['HTTP_REFERER'])


@login_required
def remove_from_cart(request, id):
	item = get_object_or_404(Product, id=id)
	order_qs = Order.objects.filter(user=request.user, ordered=False)
	if order_qs.exists(): 
		order = order_qs[0]
		#check if order item is in the order
		if order.items.filter(item__id=item.id).exists():
			order_item =  OrderItem.objects.filter(
				item=item,
				user=request.user,
				ordered=False

			)[0]
			order_item.delete()
			messages.info(request, "This item was removed from your cart.")
			# return redirect('enninapp_home')
			return redirect(request.META['HTTP_REFERER'])
		else:
			messages.info(request, "This item was not in your cart.")
			# return redirect('enninapp_home')
			return redirect(request.META['HTTP_REFERER'])
		
	else:
		# add a message saying the user doesnt have an order
		messages.info(request, "You do not have an active order.")
		# return redirect('enninapp_home')
		return redirect(request.META['HTTP_REFERER'])
	

@login_required
def CheckoutView(request, id):
	prof = Profile.objects.get(user__id = request.user.id)
	if request.method == 'POST':
		
		form = ProfileAddressForm(request.POST, instance=prof)
		if form.is_valid():
			form.save()
			return redirect(request.META['HTTP_REFERER'])
	else:
		try:
			ref = get_random_string(20)
			order = Order.objects.get(id=id)
			form = ProfileAddressForm(instance=prof)
			context = {
				'objects': order,
				'key': settings.RAVE_PUBLIC_KEY,
				'ref':ref,
				'form':form

			}
			return render(request, 'carts/checkout.html', context)
		except ObjectDoesNotExist:
			messages.error(request, "You do not have an active order")
			return redirect("/")



def edit_profile(request, id):
	prof = Profile.objects.get(user__id = request.user.id)
	if request.method == 'POST':
		form = ProfileAddressForm(request.POST, instance=prof)
		if form.is_valid():
			form.save()
			return redirect('checkout_home', id=id)

	else:
		form = ProfileAddressForm(instance=prof)
		return render(request, 'carts/edit_profile.html', {'form':form})
	


def subquantity(request, id):
	item = get_object_or_404(Product, id=id)
	order_item, created = OrderItem.objects.get_or_create(
		item=item,
		user=request.user,
		ordered=False
		)
	order_qs = Order.objects.filter(user=request.user, ordered=False)
	if order_qs.exists():
		order = order_qs[0]
		#check if order item is in the order
		if order.items.filter(item__id=item.id).exists():
			order_item.quantity -= 1
			order_item.save()
			messages.info(request, "This item quantity was update.")
			# return redirect('prod_detail', id=id)
			return redirect(request.META['HTTP_REFERER'])
		else:
			order.items.add(order_item)
			messages.info(request, "This item was added to your cart.")
			# return redirect('prod_detail', id=id)
			return redirect(request.META['HTTP_REFERER'])

	else:
		ordered_date = timezone.now()
		order = Order.objects.create(user=request.user, ordered_date=ordered_date)
		order.save()
		order.items.add(order_item)
		messages.info(request, "This item was added to your cart.")

		# return redirect('prod_detail', id=id)
		return redirect(request.META['HTTP_REFERER'])