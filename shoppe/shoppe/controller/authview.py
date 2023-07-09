from django.shortcuts import render,redirect
from django.contrib import messages
from category.forms import CustomUserForm
from django.contrib.auth import authenticate,logout,login
def register(request):
    form = CustomUserForm()
    if request.method=="POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registered Successfully! Login to Continue")
            return redirect("/login")
    context={"form":form}
    return render(request,"register.html",context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,"you  are already logged in")
        return redirect("/")
    else:
    
     if request.method=="POST":
        name=request.POST.get("username")
        passwd=request.POST.get("Password")
        user=authenticate(request,username=name,password=passwd)
    
        if user is not None:
         login(request,user)
         messages.success(request,"Logged in Successfully")
         return redirect("/")
        else:
         messages.error(request,"Invalid Username")
         return redirect("/login")
    return render(request,"loginpage.html")

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged-out successfully")
    return redirect("/")
