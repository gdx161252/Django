from django.contrib import admin
from .models import Article

# Register your models here.

#admin.site.register(Article)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    #pola w formularzu
    fields = ['title', 'content', 'year', 'image']
    #pola na liscie
    list_display = ['title', 'year']
    #pole filtra
    list_filter = ['year']
    #pole wyszukiwarki
    search_fields = ['title', 'content']
