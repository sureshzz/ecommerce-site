from django.shortcuts import render ,get_object_or_404,HttpResponse
from .models import Product
from category.models import Category
from carts.views import _cart_id
from carts.models import CartItem

# Create your views here.
def store(request,category_slug = None):
  categories = None
  products = None
  
  if category_slug != None:
    categories = get_object_or_404(Category,slug = category_slug)
    print(Category)
    print(categories)
    products = Product.objects.all().filter(category = categories,is_available = True)
    print(products)
    product_count = products.count()
  
  else:
    products = Product.objects.all().filter(is_available = True)
    product_count = products.count()
  
  
  context = {
    "products" : products,
    "productcount" : product_count
  }
  return render(request,'store/store.html',context)


def product_detail(request,category_slug,product_slug):
  print(category_slug)
  print(product_slug)
  try:
    single_product = Product.objects.get(category__slug = category_slug, slug = product_slug)
    in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request),product=single_product).exists
  except Exception as e:
    raise e
  
  context = {
    'single_product' : single_product,
    'in_cart' : in_cart,
    }
  
  return render(request,'store/product_detail.html',context)