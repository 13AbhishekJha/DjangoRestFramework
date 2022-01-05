from django.contrib import admin

from .models import Singer,Song
# Register your models here.
class SingerAdmin(admin.ModelAdmin):
    list_display=['id','name','gender']

admin.site.register(Singer,SingerAdmin)

class SongAdmin(admin.ModelAdmin):
    list_display=['id','title','singer','duration']

admin.site.register(Song,SongAdmin)