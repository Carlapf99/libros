from datetime import datetime, timedelta

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import CommentForm
from .models import Post


def post_list(request):
    posts = Post.objects.filter(is_published=True)
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    comments = post.comments.filter(is_approved=True)
    form = CommentForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        if form.cleaned_data.get('honeypot'):
            messages.error(request, 'No se pudo enviar el comentario.')
            return redirect(post.get_absolute_url())

        recent_submission = request.session.get('last_comment_at')
        now = timezone.now()
        if recent_submission:
            last_comment_at = datetime.fromisoformat(recent_submission)
            if now - last_comment_at < timedelta(minutes=1):
                messages.error(request, 'Espera un minuto antes de comentar de nuevo.')
                return redirect(post.get_absolute_url())

        comment = form.save(commit=False)
        comment.post = post
        comment.is_approved = False
        comment.save()

        request.session['last_comment_at'] = now.isoformat()
        messages.success(
            request,
            'Comentario recibido. Se publicará cuando sea aprobado por moderación.',
        )
        return redirect(post.get_absolute_url())

    return render(
        request,
        'blog/post_detail.html',
        {'post': post, 'comments': comments, 'form': form},
    )
