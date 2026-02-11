from django.contrib import admin

from .models import AuthorProfile


@admin.register(AuthorProfile)
class AuthorProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'updated_at')
    readonly_fields = ('updated_at',)
    fieldsets = (
        ('Identidad', {'fields': ('full_name', 'photo')}),
        ('Portada de inicio', {'fields': ('hero_quote',)}),
        ('Biografía', {'fields': ('biography',)}),
        ('Sistema', {'fields': ('updated_at',)}),
    )

    def has_add_permission(self, request):
        return not AuthorProfile.objects.exists()
