from django.contrib import admin
from product.models import ReadyToPress, CustomDesign, CustomDesignPhoto


# Register your models here.
class ReadyToPressAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('title', 'description')
    ordering = ('-id',)

admin.site.register(CustomDesign)
admin.site.register(CustomDesignPhoto)
admin.site.register(ReadyToPress, ReadyToPressAdmin)