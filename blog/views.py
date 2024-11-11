from django.shortcuts import get_object_or_404, render

from .models import Post


def post_list_view(request):
    posts = Post.objects.filter(status='PUB')

    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/post_detail.html', {'post': post})


def post_create_view(request):
    return render(request, 'blog/post_create.html')
