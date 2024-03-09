from django.shortcuts import render
from .models import Product

# Create your views here.
def store(request):
  products = Product.objects.all().filter(is_available = True)
  product_count = products.count()
  context = {
    "products" : products,
    "productcount" : product_count
  }
  return render(request,'store/store.html',context)