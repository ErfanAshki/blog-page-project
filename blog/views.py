from django.shortcuts import render

from .models import Post


def post_list_view(request):
    posts = Post.objects.all()

    return render(request, 'blog/post_list.html', {'posts': posts})
