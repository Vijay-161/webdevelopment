from django.shortcuts import render

from product.models import Product

# Create your views here.

def home(request):
    return render(request,"home/index.html")

def products(request):
    item = Product.objects.all()
    return render(request,"home/home.html",{'item':item})

def back(request):
    return render(request,"home/index.html")
