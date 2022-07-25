import imp
from django.shortcuts import redirect, render
from django.contrib import messages

from customer.forms import CustomerForm
from customer.models import Customer

# Create your views here.
def registerPage(request):
    return render(request,"customer/register.html")

def login(request):
    return render(request,"customer/login.html")

def save(request):
    print(request.POST)
    customer = CustomerForm(request.POST)
    customer.save()
    messages.success(request,"Customer Added Successfully")
    return redirect("/customer/login")

def login_do(request):
    if request.method == "POST":
        email = request.POST.get('username')
        pasw = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        if customer:
            if(pasw == customer.customerPasw):
               
                print("user exist")
                request.session['customer_Id']=customer.customerId
                request.session['email']=customer.customerEmail
                return redirect("/product/productPage")


            else:
                
                messages.success(request,"Password doesn't match")

        else:
            
            messages.success(request,"Invalid User")
        print(customer)

        
        
    return redirect("/customer/login")

def delete(request,id):
    data = Customer.objects.get(customerId=id)
    data.delete()
    messages.success(request,"Customer deleted")
    return redirect("/dashboard/customerdetail")