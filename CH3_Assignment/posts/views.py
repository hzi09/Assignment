from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import PostForm
from .models import Post

def home(request) :
    return render(request, 'posts/home.html')

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


@login_required
def post_create(request):
    if request.method == 'POST' :
        form = PostForm(request.POST)
        if form.is_valid() :
            post = form.save()
            return redirect('posts:post_detail', post.pk)
    else :
        form = PostForm()

    context = {
        'form' : form,
    }
    return render(request, 'posts/post_form.html', context)

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author== request.user:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save()
                return redirect('posts:post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
    
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'posts/post_form.html', context)

@require_http_methods(["GET", "POST"])
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # 요청자가 작성자인지 확인
    if post.author != request.user:
        return redirect("posts:post_list")  # 권한이 없으면 목록 페이지로 리디렉션

    if request.method == "POST":
        # POST 요청 시 삭제 수행
        post.delete()
        return redirect("posts:post_list")
    
    # GET 요청 시 삭제 확인 페이지 렌더링
    context = {
        'post': post
    }
    return render(request, "posts/post_confirm_delete.html", context)