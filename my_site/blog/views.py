from django.shortcuts import get_object_or_404, render
from datetime import date
from .models import Post, Author, Tag


def get_date(post):
    return post['date']

# Create your views here.


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, 'blog/index.html', {
        'posts': latest_posts
    })


def posts(request):
    return render(request, 'blog/all-posts.html', {
        'all_posts': Post.objects.all().order_by("-date")
    })


def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-detail.html', {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })
