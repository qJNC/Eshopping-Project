from django.http.response import JsonResponse
from django.shortcuts import redirect,render
#from django.contrib import message
from category.models import Product,cart

def addtocart(request):
    if request.method=="POST":
        if request.user.is_authenticated:
            prod_id=int(request.POST.get("product_id"))
            product_check=Product.objects.get(id=prod_id)
            if(product_check):
                if(cart.objects.filter(user=request.user.id,product_id=prod_id)):
                    return JsonResponse({"status":"Product already in cart"})
                else:
                    prod_qty=int(request.POST.get("product_qty"))
                    if product_check.product_quantity()>=prod_qty:
                        cart.objects.create(user=request.user,product_id=prod_id,product_qty=prod_qty)
                        return JsonResponse({"status":"Product added successfully"})
                    else:
                        return JsonResponse({"status":"only"+str(product_check.product_quantity)+"quantity available"})
            else:
                return JsonResponse({"status":"No such product found"})
        else:
            return JsonResponse({"status":"Login to continue"})
    return redirect("/")

def viewcart(request):
    Cart=cart.objects.filter(user=request.user)
    context={"cart":Cart}
    return render(request,"cart.html",context)

def updatecart(request):
    prod_id=int(request.POST.get("product_id"))
    if (cart.objects.filter(user=request.user,product_id=prod_id)):
        prod_qty=int(request.POST.get("product_qty"))
        Cart=cart.objects.get(product_id=prod_id,user=request.user)
        Cart.product_qty=prod_qty
        Cart.save()
        return JsonResponse({"status":"Updated Successfully"})
    return redirect("/")

def deletecartitem(request):
    if request.method=="POST":
        prod_id=int(request.POST.get("product_id"))
        if(cart.objects.filter(user=request.user,product_id=prod_id)):
            cartitem=cart.objects.get(product_id=prod_id,user=request.user)
            cartitem.delete()
            return JsonResponse({"status":"Deleted Successfully"})
    return redirect("/")

