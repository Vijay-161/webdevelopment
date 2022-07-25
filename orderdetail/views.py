from email import message
from django.shortcuts import redirect, render
from django.contrib import messages
from orderdetail.forms import OrderDetailForm
from orderdetail.models import OrderDetail

# Create your views here.
def orders(request):
    orders = OrderDetail.objects.all()

    return render(request,"orders/order.html",{'orders':orders})

def save(request):
    orderDetail = OrderDetailForm(request.POST)
    if orderDetail.is_valid():
        orderDetail.save()
        messages.success(request,"Order Successfully Done.")
    else:
        print(orderDetail.errors.as_data)
    return redirect("/product/productPage")

def deleteorder(request,id):
    orderdata = OrderDetail.objects.get(orderId=id)
    orderdata.delete()
    messages.success(request,"Order Deleted Successfully.")
    return redirect('/orderdetail/orders')

def editorder(request,id):
    order = OrderDetail.objects.get(orderId= id)
    return render(request,"orders/edit.html",{'order':order})

def updateorder(request,id):
    data = OrderDetail.objects.get(orderId=id)
    form = OrderDetailForm(request.POST,instance=data)
    form.save()
    messages.success(request,"OrderStatus Updated Successfully.")

    return redirect('/orderdetail/orders')
    