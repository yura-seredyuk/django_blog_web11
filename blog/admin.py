from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('image_show', 'title', 'author', 'created_date', 'published_date')
    list_filter = ('author', 'created_date', 'published_date')
    search_fields = ('title', 'text')
    date_hierarchy = 'published_date'
    ordering = ['author', 'published_date']

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"

    image_show.__name__ = 'images'

admin.site.register(Post, PostAdmin)