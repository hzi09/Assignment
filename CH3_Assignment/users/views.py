from django.shortcuts import get_object_or_404, render, redirect
from users.models import CustomUser
from users.forms import CustomUserCreationForm, CustomUserProfileForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required


@require_http_methods(['GET', 'POST'])
def signup(request) :
    if request.method == 'POST' :
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('posts:post_list')
    else :
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'users/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login(request) :
    if request.method == 'POST' : 
        form = AuthenticationForm(data=request.POST)
        if form.is_valid() :
            auth_login(request, form.get_user())
            next_url = request.GET.get('next') or 'posts:post_list'
            return redirect(next_url)
    
    else :
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'users/login.html', context)

@require_POST
def logout(request):
    if request.method == "POST":
        auth_logout(request)
    return redirect("posts:post_list")

@login_required
def user_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)

    if user == request.user:
        # 요청이 POST일 경우, 사용자 데이터와 제출된 파일을 포함한 폼을 생성
        if request.method == 'POST':
            form = CustomUserProfileForm(request.POST, request.FILES, instance=user)
            
            # 필드 값들이 모두 올바르면 저장하고 리디렉션
            if form.is_valid():
                form.save()
                # 수정한 후에 해당 사용자의 프로필 페이지로 리디렉션
                return redirect('users:user_profile', username=user.username) 
        # 요청이 GET일 경우
        else:
            # 사용자 데이터로 폼을 채움
            form = CustomUserProfileForm(instance=user)
    else :
        form = None

    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'users/user_profile.html', context)