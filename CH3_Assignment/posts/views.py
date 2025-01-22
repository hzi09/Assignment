from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import PostForm, CommentForm
from .models import Post, Comment

def home(request) :
    return render(request, 'posts/home.html')

def post_list(request) :
    posts = Post.objects.all().order_by('-pk')
    context = {
        "posts" : posts,
    }
    return render(request, 'posts/post_list.html', context)


def post_detail(request, pk) :
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm()
    comments = post.comments.all().order_by('-pk')

    # comment 수정 
    # GET 요청에서 'edit_comment' 쿼리 파라미터 값을 가져옴
    edit_comment = request.GET.get('edit_comment')

    try:
        # edit_comment 값이 존재하면, 정수로 변환
        # edit_comment 값이 없으면 None을 유지
        edit_comment = int(edit_comment) if edit_comment else None
    except ValueError:
        # 쿼리 파라미터 값이 숫자가 아니거나 변환할 수 없는 경우(ValueError)
        # edit_comment를 None으로 설정
        edit_comment = None

    context = {
        "post" : post,
        "comment_form" : comment_form,
        "comments" : comments,
        'edit_comment': edit_comment,
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create(request):
    if request.method == 'POST' :
        form = PostForm(request.POST)
        if form.is_valid() :
            post = form.save(commit=False)
            post.author = request.user
            post.save()
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


@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        if post.like_users.filter(pk=request.user.pk).exists():
            post.like_users.remove(request.user)   # 좋아요 취소
        else :
            post.like_users.add(request.user)      # 좋아요
        return redirect('posts:post_detail', pk=post.pk)
    return redirect('users:login')

@require_POST
def comment_create(request, pk) :
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid() :
        comment = form.save(commit=False)
        comment.post = post
        comment.comment_user = request.user
        comment.save()
        return redirect('posts:post_detail', pk=post.pk)
    return redirect('posts:post_detail', pk=post.pk)


@require_POST
def comment_delete(request, pk, comment_pk) :
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('posts:post_detail', pk=pk)


@login_required
def comment_update(request, pk, comment_pk):
    # 작성자가 현재 사용자임을 확인하며 댓글 가져오기
    comment = get_object_or_404(Comment, pk=comment_pk, comment_user=request.user)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            # 데이터베이스 저장 전 객체 반환
            updated_comment = form.save(commit=False)
            # 필드 설정
            updated_comment.post = comment.post                  # 기존 게시글 유지
            updated_comment.comment_user = comment.comment_user  # 기존 작성자 유지
            updated_comment.save()                               # 수정된 댓글 저장
            return redirect('posts:post_detail', pk=pk)
    else:
        # GET 요청 시 기존 댓글 데이터로 폼 생성
        form = CommentForm(instance=comment)

    context = {
        'form': form,
        'comment': comment,
    }
    return render(request, 'posts/comment_form.html', context)