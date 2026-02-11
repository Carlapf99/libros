from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=180)
    slug = models.SlugField(unique=True)
    cover = models.ImageField(upload_to='books/', blank=True, null=True)
    synopsis = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    purchase_url = models.URLField()
    is_featured = models.BooleanField(default=False)
    published_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'slug': self.slug})
