from django.conf import settings
from django.db import models
from enninapp.models import Product

class OrderItem(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	ordered = models.BooleanField(default=False)
	item = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)

	def __str__(self):
		return f"{self.quantity} of {self.item.name }"


	def get_total_item_price(self):
		return self.quantity * self.item.price



	def get_total_discount_item_price(self):
		return self.quantity * self.item.discount_price
		

	def get_amount_saved(self):
		return self.get_total_item_price() - self.get_total_discount_item_price()


	def get_final_price(self):
		if self.item.discount_price:
			return self.get_total_discount_item_price()
		return self.get_total_item_price()



class  Order(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	items = models.ManyToManyField(OrderItem)
	start_date = models.DateTimeField(auto_now_add=True)
	ordered_date = models.DateTimeField(auto_now_add=True)
	ordered = models.BooleanField(default=False)


	def __str__(self):
		return self.user.username



	def get_total(self):
		total = 0
		for order_item in self.items.all():
			total += order_item.get_final_price()
		return total

