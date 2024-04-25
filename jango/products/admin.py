from django.contrib import admin
from .models import Category, Product, File

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent', 'title','is_enable','created_time']
    list_filter = ['is_enable','parent']
    search_fields = ['title']

class FileInlineAdmin(admin.StackedInline):
    model = File
    fields = ['title', 'file_type', 'file','is_enable']
    extra = 0

    
@admin.register(Product)
class ProductAmin(admin.ModelAdmin):
    list_display = ['title','is_enable','created_time']
    list_filter = ['is_enable']
    search_fileds = ['title']
    filter_horizontal = ['categories']
    inlines = [FileInlineAdmin] 