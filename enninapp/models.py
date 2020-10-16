from django.db import models
from django.urls import reverse

class Category(models.Model):
	name = models.CharField(max_length = 100)
	slug = models.SlugField(max_length = 50, unique=True, help_text='Unique value for product page URl, created from name.')
	description = models.TextField()
	is_active = models.BooleanField(default = True)
	meta_keywords = models.CharField("Meta keywords", max_length=255, help_text='comma-delimited set of SEO keywords for meta tag')
	meta_description = models.CharField("Meta Description", max_length=255, help_text='Content for description meta tag')
	created_at = models.DateTimeField(auto_now_add=True)
	Updated_at = models.DateTimeField(auto_now_add=True)


	class Meta:
		db_table ='categories'
		ordering = ['-created_at']
		verbose_name_plural = 'Categories'



	def __str__(self):
		return self.name

	
	def get_absolute_url(self):
		return reverse('enninapp_category', (), {'category_slug': self.slug})



class Brand(models.Model):
	name = models.CharField(max_length=100)
	image = models.FileField()

	def __str__(self):
		return self.name




class Product(models.Model):
	name = models.CharField(max_length=255, unique=True)
	slug = models.SlugField(max_length = 50, unique=True, help_text='Unique value for product page URl, created from name.')
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True, related_name='products')
	price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.00)
	new_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.00)
	quantity = models.IntegerField(default=1)
	image = models.FileField()
	image1 = models.FileField(default='default.jpg')
	image2 = models.FileField(default='default.jpg')
	image3 = models.FileField(default='default.jpg')
	is_active = models.BooleanField(default=True)
	is_featured = models.BooleanField(default=False)
	description = models.TextField()
	meta_description = models.CharField("Meta Description", max_length=255, help_text='Content for description meta tag')
	meta_keywords = models.CharField("Meta keywords", max_length=255, help_text='comma-delimited set of SEO keywords for meta tag')
	created_at = models.DateTimeField(auto_now_add=True)
	Updated_at = models.DateTimeField(auto_now_add=True)
	discount_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.00)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='products')
	



	class Meta:
		db_table = 'product'
		ordering = ['-created_at']



	def __str__(self):
		return self.name


	def get_absolute_url(self):
		return reverse('product_detail', kwargs= {'slug': self.slug})


	def get_add_to_cart_url(self):
		return reverse('add_to_cart', kwargs= {'slug': self.slug})

	def get_remove_from_cart_url(self):
		return reverse('remove_from_cart', kwargs= {'slug': self.slug})

	
	def sale_price(self):
		if self.old_price > self.price:
			return self.price
		else:
			return None




		 
class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        	return self.email




