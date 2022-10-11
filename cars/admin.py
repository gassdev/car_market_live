from django.contrib import admin

from .models import Car
from django.utils.html import format_html

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(f'<img src="{object.photo.url}" style="border-radius:50px;" width="40" />')
    
    thumbnail.short_description = 'Car Image'
    list_display = ('id', 'thumbnail', 'car_title', 'brand', 'color', 
                    'model', 'year', 'fuel_type', 'is_featured', 
                    'created_at')
    list_display_links = ('id', 'thumbnail', 'car_title')
    list_editable = ('is_featured',)
    search_fields = ('id', 'car_title', 'model', 'fuel_type')
    list_filter = ('brand', 'color', 'fuel_type', 'year')
    

admin.site.register(Car, CarAdmin)