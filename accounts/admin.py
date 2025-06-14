from django.contrib import admin
from . import models
from import_export import resources
from import_export.admin import ExportActionMixin


# Register your models here.

class ExpCustomer(resources.ModelResource):
    class Meta:
        model = models.Customer
        fields = ('id','name','phone','email','date_created')

class CustomerAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ['id','name','phone','email','date_created']
    list_filter = ['date_created']
    search_fields =['name']
    date_hierarchy = 'date_created'
    list_per_page = 2
    resource_class =ExpCustomer


admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Image)
admin.site.register(models.ImageType)
admin.site.register(models.Menu)
admin.site.register(models.MenuDetail)

admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.ProductDetail)
admin.site.register(models.ProductDetailImage)
