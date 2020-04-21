from django.contrib import admin

from .models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
    search_fields = ['username']
    list_filter = ['username']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', "author", "publish_time"]
    search_fields = ['title', "publish_time", "content"]
    list_filter = ["title", "publish_time"]


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
