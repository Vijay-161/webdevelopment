
from django.shortcuts import redirect, render
from product.forms import ProductForm
from product.models import Product
from customer.models import Customer
from django.views import View
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def productPage(request):
    return render(request,"product/product.html")


def details(request,id):
    customerDetail = Customer.objects.all()
    detail ={}
    detail['productDetail']= Product.objects.get(productId=id)
    customer = request.session.get('email')
    detail['customerEmail'] = request.session.get('email')
    detail['customerDetail'] =Customer.objects.get(customerEmail = customer)

    return render(request,"product/details.html",detail)

def buy(request,id):
    # data = Product.objects.get(id=id)
    # form = ProductForm(request.POST,request.FILES,instance=data)
    # form.save()

    return redirect("details")

def logout(request):
    request.session.clear()

    return redirect("home")


# class productPage(View):
    

#     def get(self, request):
       
            
                
#         allproduct = Product.objects.all()
#         data={}
#         data['email']=request.session.get('email')
#         data['products'] = allproduct
#         data['customerId']=request.session.get('customer_Id')
#         print(allproduct)
#         ('you are:',request.session.get('email'))
#         print('id',request.session.get('customer_Id'))
#         return render(request,"product/product.html",data)

login_required()
def productPage(request):
    allproduct = Product.objects.all()
    data={}
    data['email']=request.session.get('email')
    data['products'] = allproduct
    data['customerId']=request.session.get('customer_Id')
    print(allproduct)
    print('you are:',request.session.get('email'))
    print('id',request.session.get('customer_Id'))
    return render(request,"product/product.html",data)
    