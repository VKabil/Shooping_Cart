from django.contrib import admin
from .models import *
# Register your models here.

# class CatagoryAdmin(admin.ModelAdmin):
#     list_display =('name', 'images', 'description', 'created_at')
# admin.site.register(Catagory, CatagoryAdmin)


admin.site.register(Catagory)
admin.site.register(Product)
