from django.contrib import admin
from . models import Cart, CartItem

class CardAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')

class CardItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')

# Register your models here.
admin.site.register(Cart, CardAdmin)
admin.site.register(CartItem, CardItemAdmin)