from django.contrib import admin
from .models import Post,Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'date_posted')
#     list_filter = ('date_posted', 'author')
#     search_fields = ('title', 'content', 'author')