from django.contrib import admin

# Register your models here.
from category.models import Services,Product,cart,Order,OrderItem,profile


admin.site.register(Services)
admin.site.register(Product)
admin.site.register(cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(profile)