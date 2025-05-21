from django.contrib import admin
from .models import Article

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'is_published',)
    list_filter = ('title',)
    search_fields = ('title',)