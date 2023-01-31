from django.contrib import admin
from .models import *
# Register your models here.



class PostAdmin(admin.ModelAdmin):

    list_display = ('user', 'title', 'category','id')
    list_filter = ('date_now',)
    search_fields = ('title','category','id')


class CommentAdmin(admin.ModelAdmin):

    list_display = ('user', 'title','id')
    list_filter = ('date_now',)
    search_fields = ('title','id')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tagname)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Contacts)