from django.contrib import messages
from django.shortcuts import render,redirect
from product.forms import ProductForm
from customer.models import Customer
from product.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.

login_required()
def view(request):
    
    return render(request,"dashboard/dashboard.html")
login_required()
def dashboard(request):
    
    return render(request,"dashboard/dashboard.html")

def save(request):
    data = ProductForm(request.POST,request.FILES)
    data.save()
    messages.success(request,"Product Added Successfully.")
    return redirect('/dashboard/productdetail')

def customerdetail(request):
    customers = Customer.objects.all()
    return render(request,"dashboard/customerDetail.html",{'check':customers})

def productdetail(request):
    products = Product.objects.all()
    return render(request,"dashboard/productDetail.html",{'product':products})

def deleteProduct(request,id):
    data = Product.objects.get(productId=id)
    data.delete()
    messages.success(request,"Product Deleted Successfully.")
    return redirect('/dashboard/productdetail')

def editProduct(request,id):
    data = Product.objects.get(productId=id)

    return render(request,"dashboard/editProduct.html",{'data':data})

def updateProduct(request,id):
    data = Product.objects.get(productId=id)
    form = ProductForm(request.POST,request.FILES,instance=data)
    form.save()
    messages.success(request,"Product Updated Successfully.")

    return redirect('/dashboard/productdetail')