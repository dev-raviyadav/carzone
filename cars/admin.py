from django.contrib import admin
from .models import Car
from django.utils.html import format_html


class CarAdmin(admin.ModelAdmin):
    
    def thumbnail(self, obj):
        return format_html(
            '<img src="{}" width="40" style="border-radius: 100%;" />',
            obj.car_photo.url
        )

    thumbnail.short_description = 'Photo'
    list_display = (
        'id',
        'thumbnail',
        'car_title',
        'city',
        'color',
        'model',
        'year',
        'body_style',
        'fuel_type',
        'is_featured',
    )

    list_display_links = (
        'id',
        'thumbnail',
        'car_title',
    )

    list_editable = (
        'is_featured',
    )   

    search_fields = (
        'id',
        'car_title',
        'city',
        'model',
        'body_style',
        'fuel_type',
    )

    list_filter = (
        'model',
        'city',
        'body_style',
        'fuel_type',
    )

# Register your models here.
admin.site.register(Car, CarAdmin)