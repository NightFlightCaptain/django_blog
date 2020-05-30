from django.contrib import admin

# Register your models here.
from my_blog.models import Tag, Article

admin.site.site_header = '后台管理'
admin.site.site_title = 'Blog后台管理'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_by', 'created_on', 'is_deleted', 'state')
    list_per_page = 30
    ordering = ('-created_on',)
    list_display_links = ('id', 'name')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'desc', 'content', 'cover_image', 'created_on', 'created_by', 'is_deleted', 'state', 'tag_id')

    list_per_page = 30
    ordering = ('-id',)
    list_display_links = ('id', 'title')

    def delete(self, request, queryset):
        queryset.update(is_deleted=True)


    delete.short_description = "删除所选文章"
    actions = [delete, ]

    search_fields = ['title','desc','content']

    list_filter = ['created_by', 'state', 'tag_id']

    date_hierarchy = 'created_on'
