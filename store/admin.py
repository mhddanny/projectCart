from django.contrib import admin
from . models import Product, Variation

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Admin View for Product'''

    list_display = ('product_name', 'price', 'stock', 'category', 'modifield_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    # list_filter = ('',)
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'varian_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'varian_category', 'variation_value')
admin.site.register(Variation, VariationAdmin)