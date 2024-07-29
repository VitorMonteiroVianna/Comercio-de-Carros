from django.contrib import admin
from cars.models import Brand, Cars



class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand')
    search_fields = ('id', 'brand')


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'brand', 'color', 'factory_yaer', 'model_yaer', 'value')
    search_fields = ('id', 'model')


admin.site.register(Brand, BrandAdmin)
admin.site.register(Cars, CarAdmin)

