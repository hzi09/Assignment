from django.shortcuts import get_object_or_404, render
from .models import Post

def post_list(request) :
    posts = Post.objects.all().order_by('-pk')
    context = {
        "posts" : posts,
    }
    return render(request, 'posts/post_list.html', context)

def post_detail(requset, pk) :
    post = get_object_or_404(Post, pk=pk)
    context = {
        "post" : post,
    }
    return render(requset, 'posts/post_detail.html', context)