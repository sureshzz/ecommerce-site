from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

def home(request):
  Products = Product.objects.all().filter(is_available= True)
  print(Products)
  context = {
    'products' :  Products,
  }
  return render(request,'home.html',context)
  # return HttpResponse("hello")
