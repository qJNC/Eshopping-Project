"""shoppe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings               
from django.conf.urls.static import static 

from shoppe import views
from shoppe.controller import authview,cart,checkout,order

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.homepage),
    path("about-us/",views.aboutUs),
    path("course/<courseid>",views.course),
    
    path("services/",views.service,name="service"),
    path("Collections/<str:slug>",views.Products,name="Product"),
    path("fruits/",views.Fruits ,name="Fruits"),
    path("collections/<str:cate_slug>/<str:prod_slug>",views.productview,name="Productview"),
    
    path("register/",authview.register,name="register"),
    path("login/",authview.loginpage,name="loginpage"),
    path("logout/",authview.logoutpage,name="logout"),

    path("add-to-cart",cart.addtocart, name="addtocart"),
    path("update-cart",cart.updatecart,name="updatecart"),
    path("viewcart",cart.viewcart,name="viewcart"),

    path("checkout",checkout.index,name="checkout"),
    path("place-order",checkout.placeorder,name="Placeorder"),
    
    path("orderdetails/",order.index,name="orderdetails"),
    path("view-order/<str:t_no>",order.vieworders,name="orderview")
]

if settings.DEBUG:
   urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
