
import re
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def registerAdmin(request):
    if request.method == "POST":
        print(request.POST)
        User.objects.create_user(
            first_name =request.POST['firstName'],
            last_name = request.POST['lastName'],
            email = request.POST['email'],
            username = request.POST['username'],
            password = request.POST['password'],

        )
        
    else:
        return render(request,"adminStaff/aregister.html")

    return render(request,"adminStaff/aregister.html")


def loginAdmin(request):
    if request.method == "POST":
        user = authenticate(request,
        username = request.POST['username'],
        password = request.POST['password'])
        print(user)

        if user is not None:
            login(request,user)

            return redirect("/dashboard/view")
        
        else:
        
            return redirect("/adminStaff/login")
    else:
        return render(request,"adminStaff/alogin.html")

def logout_fn(request):
    logout(request)
    return redirect("home")
        
    