from . import views
from django.urls import path,include
from .views import *

urlpatterns = [
    path("",views.home,name = 'home'),
    path("register/",register,name = 'register'),  
    path("login/",login,name = 'login'), 
    path('invoice/',create_invoice,name='create_invoice'),
    path("viewinvoice/",viewinvoice,name = 'viewinvoice'),
    path("deleteinvoice/<int:pk>",deleteinvoice,name = 'deleteinvoice'),

    

    ]