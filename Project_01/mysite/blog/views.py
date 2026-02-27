
from django.shortcuts import render, get_object_or_404
from .models import Post


# Show only published posts (using custom manager)
def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


# Detail view (only published)
def post_detail(request, id):
    post = get_object_or_404(
        Post.published,
        id=id
    )
    return render(request, 'blog/post_detail.html', {'post': post})


#  Show all posts (including drafts)
def post_all(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_all.html', {'posts': posts})