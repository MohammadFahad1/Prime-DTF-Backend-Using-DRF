from django.contrib import admin
from product.models import ReadyToPress, CustomDesign, CustomDesignPhoto, ProductType, Product, ProductColor, ProductImage


# Register your models here.
class ReadyToPressAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('title', 'description')
    ordering = ('-id',)

admin.site.register(ReadyToPress, ReadyToPressAdmin)
admin.site.register(CustomDesign)
admin.site.register(CustomDesignPhoto)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(ProductColor)
admin.site.register(ProductImage)