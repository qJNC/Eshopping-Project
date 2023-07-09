from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from category.models import Services
from category.models import Product
from django.contrib import messages  
def homepage(request):
    data={
        "title":"home new",
        "clist" :["php","java","django"]
    }
    return render(request,"index.html")

def aboutUs(request):
    return render( request,"home.html")

def course(request,courseid):
    return HttpResponse(courseid)

def service(request):
     servicedata=Services.objects.all()
     data={"servicename":servicedata}
     return render(request,"service.html",data)


def Products(request,slug):
     if (Services.objects.filter(serv_name=slug ,serv_status=0)) :
        products= Product.objects.filter(category__serv_name=slug)
        category_name=Services.objects.filter(serv_name=slug).first()
        data={"servicesname":category_name,
            "Products":products}
        return render(request,"products.html",data)
     else :
        messages.warning(request,"No such category Found")

        return HttpResponseRedirect("services")

def productview(request,cate_slug,prod_slug):
     if(Services.objects.filter(serv_name=cate_slug,serv_status=0)):
        if(Product.objects.filter(product_name=prod_slug,product_status=0)):
            products=Product.objects.filter(product_name=prod_slug,product_status=0).first()
            context={"products":products}
        else:
            messages.error(request,"No such products Found")
            return HttpResponseRedirect("Services")
     else:
            messages.error(request,"No such products Found")
            return HttpResponseRedirect("Product")
     return render(request,"view.html",context)
    
def Fruits(request):
    return render(request,"fruits.html")