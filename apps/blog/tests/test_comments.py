from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from apps.blog.models import Comment, Post


class CommentModerationTests(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title='Post de prueba',
            slug='post-de-prueba',
            excerpt='Extracto',
            content='Contenido de prueba',
            is_published=True,
            published_at=timezone.now(),
        )

    def test_new_comment_is_pending(self):
        response = self.client.post(
            reverse('post_detail', kwargs={'slug': self.post.slug}),
            {
                'name': 'Lector',
                'body': 'Este comentario tiene longitud suficiente.',
                'honeypot': '',
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        comment = Comment.objects.get(post=self.post)
        self.assertFalse(comment.is_approved)
