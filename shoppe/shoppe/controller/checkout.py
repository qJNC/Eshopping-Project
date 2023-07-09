from django.shortcuts import redirect,render
from django.contrib import messages
from category.models import Product,cart,Order,OrderItem,profile
from django.contrib.auth.decorators import login_required
import random
from django.contrib.auth.models import User
@login_required(login_url="loginpage")
def index(request):
    raw_cart=cart.objects.filter(user=request.user)
    for item in raw_cart:
        if item.product_qty > item.product.product_quantity:
            cart.objects.delete(id=item.id)
    cartitem=cart.objects.filter(user=request.user)
    total_price=0
    for items in cartitem:
        total_price=total_price+item.product.product_Selling_price*item.product_qty
    userprofile=profile.objects.filter(user=request.user).first()
    context={"cartitems":cartitem,"userprofile":userprofile,"total_price":total_price}
    return render(request,"checkout.html",context)

@login_required(login_url="loginpage")
def placeorder(request):
    if request.method=="POST":
        neworder=Order()
        neworder.user=request.user
        neworder.fname=request.POST.get("fname")
        neworder.lname=request.POST.get("lname")
        neworder.email=request.POST.get("email")
        neworder.phone=request.POST.get("phone")
        neworder.address=request.POST.get("address")
        neworder.city=request.POST.get("city")
        neworder.state=request.POST.get("state")
        neworder.country=request.POST.get("country")
        neworder.pincode=request.POST.get("pincode")
        neworder.payment_mode=request.POST.get("payment_mode")
        cart=cart.objects.filter(user=request.user)
        cart_total_price=0
        for item in cart:
            cart_total_price=cart_total_price+item.product.product_selling_price*item.product_qty
            neworder.tatal_price=cart_total_price
        tacking_no="lname"+str(random.randint(1111111,9999999))
        while Order.objects.filter(tracking_no=tacking_no) is None:
            tacking_no="lname"+str(random.randint(1111111,9999999))
        neworder.tracking_no=tacking_no
        neworder.save()
        neworderitems=cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order=neworder,
                products=item.product,
                price=item.product.product_selling_price,
                quantity=item.product_qty
            )
            #to decrease & increase product quantity stock
            orderproduct=Product.objects.filter(id=item.product_id).first()
            orderproduct.product_quantity=orderproduct.product_quantity-item.product_qty
            orderproduct.save()

            #to clear user cart
            cart.object.filter(user=request.user).delete()
            messages.success(request,"Your order has been placed successfully")
        return redirect("/")


def placeorder(request):
    if request.method=="POST":
        currentuser=User.objects.filter(id=request.user.id).first()
        if not currentuser.first_name:
            currentuser.first_name=request.POST.get("fname")
            currentuser.last_name=request.POST.get("lname")
            currentuser.save()
        if not profile.objects.filter(user=request.user):
            userprofile=profile()
            userprofile.user=request.user
            userprofile.phone=request.POST.get("phone")
            userprofile.address=request.POST.get("address")
            userprofile.city=request.POST.get("city")
            userprofile.state=request.POST.get("state")
            userprofile.country=request.POST.get("country")
            userprofile.pincode=request.POST.get("pincode")
            userprofile.save()


