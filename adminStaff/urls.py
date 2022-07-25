from django.urls import path
from adminStaff import views

urlpatterns = [
   
    path("registerAdmin",views.registerAdmin),
    path("login",views.loginAdmin),
    path("logout",views.logout_fn),
   
]