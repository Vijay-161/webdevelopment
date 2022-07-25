from django.urls import path
from orderdetail import views

urlpatterns = [
    
    path("orders",views.orders),
    path("saveorder",views.save),
    path("deleteorder/<int:id>",views.deleteorder),
    path("editorder/<int:id>",views.editorder),
    path("updateorder/<int:id>",views.updateorder),
    
]