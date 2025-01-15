from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostForm
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



def post_create(request):
    if request.method == 'POST' :
        form = PostForm(request.POST)
        if form.is_valid() :
            post = form.save()
            return redirect('posts:post_detail', post.pk)
    else :
        form = PostForm

    context = {
        'form' : form,
    }
    return render(request, 'posts/post_form.html', context)

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(post.title)
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


def post_delete(request, pk) : 
    # 삭제할 post 객체를 가져오기
    post = get_object_or_404(Post, pk=pk)

    # POST 요청이 오면 삭제
    if request.method == "POST":
        post.delete()
        # 삭제 후에 목록 페이지로
        return redirect("posts:post_list")
    # GET 요청이 오면 삭제 확인 페이지
    context = {
        'post' : post
    }
    return render(request, "posts/post_confirm_delete.html", context)