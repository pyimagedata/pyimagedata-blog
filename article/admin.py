from django.contrib import admin
from .models import Article,Category, Tag

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','id']
    list_display_links = ['title','id']
    
    class Meta:
        model = Category

@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','id']
    list_display_links = ['title','id']
    
    class Meta:
        model = Tag

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['author','category','title','publishing_date','hit','id']
    list_display_links = ['author','category','title','publishing_date','id']
    list_filter = ['author','category','publishing_date','hit']
    search_fields = ['author','category','title','content']
    class Meta:
        model = Article

