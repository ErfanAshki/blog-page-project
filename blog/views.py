from django.shortcuts import get_object_or_404, render, redirect

from .models import Post
from .forms import NewPostForm


def post_list_view(request):
    posts = Post.objects.filter(status='PUB').order_by('-datetime_modified')

    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/post_detail.html', {'post': post})


def post_create_view(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            form = NewPostForm()
            return redirect('post_list')
    else:
        form = NewPostForm()

    return render(request, 'blog/post_create.html', {'form': form})


def post_update_view(request, pk):
    post = get_object_or_404(Post, pk=pk)

    form = NewPostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_list')

    return render(request, 'blog/post_create.html', {'form': form})


def post_delete_view(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('post_list')

    return render(request, 'blog/post_delete.html', {'post': post})


