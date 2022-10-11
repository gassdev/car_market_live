from django.contrib import admin
from .models import Team
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(f'<img src="{object.photo.url}" style="border-radius:50px;" width="40" />')
    
    thumbnail.short_description = 'Photo'
        
    list_display = ('id', 'thumbnail', 'full_name', 'designation', 'created_date')
    list_display_links = ('id', 'thumbnail', 'full_name')
    search_fields = ('first_name', 'last_name', 'designation')
    list_filter = ('designation', 'created_date')

admin.site.register(Team, TeamAdmin)