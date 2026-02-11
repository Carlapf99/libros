from django.contrib import admin

from .models import AuthorProfile


@admin.register(AuthorProfile)
class AuthorProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'updated_at')

    def has_add_permission(self, request):
        return not AuthorProfile.objects.exists()
