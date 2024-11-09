from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'datetime_created', 'datetime_modified', 'status']
    ordering = ['id']


admin.site.register(Post, PostAdmin)

