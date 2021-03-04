from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html

# Register your models here.

class YtAdmin(admin.ModelAdmin):
    def YT_Photo(self,object):
        return format_html('<img src="{}" width="60" height="60" />'.format(object.photo.url))
    list_display = ('id','first_name','YT_Photo','subs_count','is_featured')
    search_fields = ('first_name', 'last_name','category')
    list_filter = ('city','camera_type')
    list_display_links = ('id','first_name')
    list_editable = ('is_featured',)


admin.site.register(Youtuber,YtAdmin)