from django.core.exceptions import ValidationError
from django.db import models


class AuthorProfile(models.Model):
    full_name = models.CharField(max_length=150)
    hero_quote = models.CharField(max_length=255)
    biography = models.TextField()
    photo = models.ImageField(upload_to='author/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Perfil del autor'
        verbose_name_plural = 'Perfil del autor'

    def clean(self):
        if not self.pk and AuthorProfile.objects.exists():
            raise ValidationError('Solo puede existir un perfil de autor.')

    def __str__(self):
        return self.full_name
