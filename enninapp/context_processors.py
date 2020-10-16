def categories(request):
    from .models import Category
    return {'category':Category.objects.all()}


def order(request):
	from carts.models import Order
	return {'orders':Order.objects.get(user=request.user, ordered=False)}