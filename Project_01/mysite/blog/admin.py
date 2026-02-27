from django.contrib import admin

# Register your models here.
from.models import Post
# admin.site.register(post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','publish','created','updated','author']  #show these fields in admin panel
    list_filter = ['publish','created','author']  #filter by these fields in admin panel
    search_fields = ['title','body']  #search by these fields in admin panel
    prepopulated_fields = {'slug':('title',)}  #automat
    raw_id_fields = ['author']  #show author name instead of id in admin panel
    date_hierarchy = 'publish'  #show date hierarchy in admin panel
    ordering = ['title']   
