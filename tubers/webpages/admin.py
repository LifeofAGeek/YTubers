from django.contrib import admin
from .models import Slider, team
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):

    def Myphoto(self,object):
        return format_html('<img src="{}" width="60" height="60" />'.format(object.photo.url))

    list_display = ('id', 'Myphoto' ,'first_name', 'role', 'created_date')
    list_display_links = ('first_name', 'id')
    search_fields = ('first_name', 'role')
    list_filter = ('role',)


# Register your models here.
admin.site.register(Slider)
admin.site.register(team,TeamAdmin)