from django.urls import path
from dashboard import views

urlpatterns = [
    
    path("view",views.view),
    path("dashboard",views.dashboard),
    path("save",views.save),
    path("customerdetail",views.customerdetail),
    path("productdetail",views.productdetail),
    path("deleteProduct/<int:id>",views.deleteProduct),
    path("editProduct/<int:id>",views.editProduct),
    path("updateProduct/<int:id>",views.updateProduct),

    
]