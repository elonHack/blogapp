from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.
def home(request):

    all_posts = Post.objects.exclude(status='draft')
    return render(request, 'blog/index.html', context={'posts':all_posts})

def detailed_post(request, post):
    post = get_list_or_404(Post, slug=post, status='published')[0]
    return render(request, 'blog/single.html', context={"post":post})