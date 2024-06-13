from django.contrib import admin
from store.models import *
# Register your models here.

class OrderItemTublarinline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTublarinline]


admin.site.register(CatagoryItems)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Review)

