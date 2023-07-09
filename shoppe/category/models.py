from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Services(models.Model):    
  
  serv_image=models.FileField(upload_to="service",max_length=250,default=None) 
  serv_name=models.CharField(max_length=50)
  serv_desc=models.TextField(max_length=500)
  serv_status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
  serv_Trending=models.BooleanField(default=False,help_text="0=default,1=Trending")
  serv_meta_title=models.CharField(max_length=50)
  serv_meta_keyword=models.CharField(max_length=50,default=None)
  serv_meta_description=models.CharField(max_length=50,null=False)
  
  def _str_(self):
    return self.name

class Product(models.Model):
    category= models.ForeignKey(Services, on_delete=models.CASCADE)
    
    product_image=models.FileField(upload_to="service",max_length=250,null=True,default=None) 
    product_name=models.CharField(max_length=50,null=False,blank=False)
    product_desc=models.TextField(max_length=500,null=False,blank=False,default=None)
    product_status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    product_Trending=models.BooleanField(default=False,help_text="0=default,1=Trending")
    product_meta_title=models.CharField(max_length=50,null=False,blank=False)
    product_meta_keyword=models.CharField(max_length=50,null=False,blank=False)
    product_meta_description=models.CharField(max_length=50,null=False,blank=False)
    product_small_description=models.CharField(max_length=50,null=False,blank=False)
    product_quantity=models.IntegerField(null=False,blank=False)
    product_original_price=models.FloatField(null=False,blank=False)
    product_Selling_price=models.FloatField(null=False,blank=False)
    product_tag=models.CharField(max_length=50,null=False,blank=False)
    
    def _str_(self):
     return self.name

class cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fname=models.CharField(max_length=150,null=False)
    lname=models.CharField(max_length=150,null=False)
    email=models.CharField(max_length=150,null=False)
    phone=models.CharField(max_length=150,null=False)
    Address=models.TextField(null=False)
    city=models.CharField(max_length=150,null=False)
    state=models.CharField(max_length=150,null=False)
    country=models.CharField(max_length=150,null=False)
    pincode=models.CharField(max_length=150,null=False)
    total_price=models.FloatField(null=False)
    payment_mode=models.CharField(max_length=150,null=False)
    payment_id=models.CharField(max_length=250,null=False)
    orderstatus=(
        ("Pending","Pending"),
        ("Out for Shipping","Out for Shipping"),
        ("Completed","Completed")
    )
    status=models.CharField(max_length=150,choices=orderstatus,default="Pending")
    message=models.TextField(null=True)
    tracking_no=models.CharField(max_length=150,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return "{}-{}".format(self.id,self.tracking_no)

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.FloatField(null=False)
    quantity=models.IntegerField(null=False)

    def __str__(self):
        return "{} {}".format(self.order.id,self.order.tracking_no)

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=150,null=False)
    address=models.TextField(null=False)
    city=models.CharField(max_length=150,null=False)
    state=models.CharField(max_length=150,null=False)
    country=models.CharField(max_length=150,null=False)
    pincode=models.CharField(max_length=150,null=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
