from django.urls import path
from product import views
from product.views import productPage


urlpatterns = [
    
    # path("",productPage.as_view(),name="products"),
    # path("productPage",productPage.as_view(),name='productPage'),
    path("productPage",views.productPage,name='productPage'),
    path("logout",views.logout,name='logout'),
    path("details/<int:id>",views.details,name='details'),
    path("buy/<int:id>",views.details,name='buy'),
    
    
]