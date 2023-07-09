from django.shortcuts import redirect,render
from django.contrib import messages
from category.models import Product,cart,Order,OrderItem,profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    orders=Order.objects.filter(user=request.user)
    context={"orders":orders}
    return render(request,"orderindex.html",context)

def vieworders(request,t_no):
    order=Order.objects.filter(tracking_no=t_no)
    orderitem=OrderItem.objects.filter(order=order)
    context={"order":order,"orderitems":orderitem}
    return render(request,"vieworder.html",context)