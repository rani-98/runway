from django.contrib import admin
from .models import Cart, Address, Order, OrderShirt


class OrderShirtInline(admin.TabularInline):
    model = OrderShirt

    # add functionality to the inline
    def has_add_permission(self, request, obj=None):
        return False


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderShirtInline,
    ]
    
    # disable edit functionality
    def has_change_permission(self, request, obj=None):
        return False


# Register your models here.
admin.site.register(Cart)
admin.site.register(Address)
admin.site.register(Order, OrderAdmin)