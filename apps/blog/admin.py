from django.contrib import admin
from django.utils import timezone

from .models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'published_at', 'created_at')
    list_filter = ('is_published', 'published_at')
    search_fields = ('title', 'excerpt', 'content')
    prepopulated_fields = {'slug': ('title',)}
    actions = ('publish_posts', 'unpublish_posts')

    @admin.action(description='Publicar artículos seleccionados')
    def publish_posts(self, request, queryset):
        queryset.update(is_published=True, published_at=timezone.now())

    @admin.action(description='Despublicar artículos seleccionados')
    def unpublish_posts(self, request, queryset):
        queryset.update(is_published=False)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'created_at')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments', 'reject_comments']

    @admin.action(description='Aprobar comentarios seleccionados')
    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)

    @admin.action(description='Dejar comentarios en pendiente')
    def reject_comments(self, request, queryset):
        queryset.update(is_approved=False)
