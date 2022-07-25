from django.urls import path
from customer import views

urlpatterns = [
    # path("",views.login),
    path("login",views.login),
    path("registerPage",views.registerPage),
    path("save",views.save),
    path("login_do",views.login_do),
    path("delete/<int:id>",views.delete),
]