from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'price', 'published_date', 'created_at')
    list_filter = ('is_featured', 'published_date', 'created_at')
    search_fields = ('title', 'synopsis')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_featured', 'price')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Información principal', {'fields': ('title', 'slug', 'cover', 'synopsis')}),
        ('Comercial', {'fields': ('price', 'purchase_url')}),
        ('Publicación', {'fields': ('is_featured', 'published_date', 'created_at')}),
    )
