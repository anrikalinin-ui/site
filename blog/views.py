from django.shortcuts import render

from .models import Post


def post_list(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk, published=True)
    return render(request, 'blog/post_detail.html', {'post': post})
