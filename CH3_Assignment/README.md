# 1. User와 Post 앱 개발 (MTV 패턴)

## 🗂️Directory Structure
```
📦CH3_Assignment                            # Django 프로젝트 루트 디렉토리
 ┣ 📂media                                  # 업로드된 파일 및 미디어 파일 저장 디렉토리
 ┃ ┗ 📜default.png                          # 기본 이미지 파일 (예: 사용자 기본 프로필 사진)
 ┣ 📂my_pjt                                 # Django 프로젝트 설정 디렉토리
 ┃ ┣ 📜asgi.py                              # ASGI 서버 설정 파일
 ┃ ┣ 📜settings.py                          # Django 설정 파일 (데이터베이스, 앱, 미들웨어 등 포함)
 ┃ ┣ 📜urls.py                              # 전역 URL 라우팅 설정 파일
 ┃ ┣ 📜wsgi.py                              # WSGI 서버 설정 파일
 ┃ ┗ 📜__init__.py                          # Python 패키지 초기화 파일
 ┣ 📂posts                                  # 게시물 관리와 관련된 앱 디렉토리
 ┃ ┣ 📂migrations                           # 데이터베이스 마이그레이션 파일 디렉토리
 ┃ ┃ ┣ 📜0001_initial.py                    # 초기 마이그레이션 파일
 ┃ ┃ ┣ 📜0002_post_author.py                # 게시물 작성자 추가 마이그레이션
 ┃ ┃ ┣ 📜0003_post_like_users.py            # 좋아요 기능 추가 마이그레이션
 ┃ ┃ ┣ 📜0004_comment.py                    # 댓글 모델 추가 마이그레이션
 ┃ ┃ ┣ 📜0005_comment_comment_user.py       # 댓글 작성자 추가 마이그레이션
 ┃ ┃ ┗ 📜__init__.py                        # 마이그레이션 초기화 파일
 ┃ ┣ 📂templates                            # 게시물 앱 전용 템플릿 파일 디렉토리
 ┃ ┃ ┗ 📂posts                              # 템플릿 세부 디렉토리
 ┃ ┃   ┣ 📜home.html                        # 홈 화면 템플릿
 ┃ ┃   ┣ 📜post_confirm_delete.html         # 게시물 삭제 확인 페이지
 ┃ ┃   ┣ 📜post_detail.html                 # 게시물 상세 페이지 템플릿
 ┃ ┃   ┣ 📜post_form.html                   # 게시물 작성/수정 폼 템플릿
 ┃ ┃   ┗ 📜post_list.html                   # 게시물 목록 템플릿
 ┃ ┣ 📜admin.py                             # 게시물 앱 관리자 페이지 설정
 ┃ ┣ 📜apps.py                              # 게시물 앱 설정 파일
 ┃ ┣ 📜forms.py                             # 게시물 관련 폼 정의
 ┃ ┣ 📜models.py                            # 게시물 및 관련 데이터베이스 모델 정의
 ┃ ┣ 📜tests.py                             # 게시물 앱 테스트 코드 작성
 ┃ ┣ 📜urls.py                              # 게시물 앱 URL 라우팅 설정
 ┃ ┣ 📜views.py                             # 게시물 관련 뷰 함수/클래스 정의
 ┃ ┗ 📜__init__.py                          # Python 패키지 초기화 파일
 ┣ 📂static                                 # 정적 파일 디렉토리
 ┃ ┣ 📂css                                  # CSS 파일 디렉토리
 ┃ ┃ ┗ 📜styles.css                         # 공통 스타일 정의 파일
 ┣ 📂templates                              # 공통 템플릿 디렉토리
 ┃ ┣ 📜base.html                            # 공통 레이아웃 템플릿 (헤더, 푸터 포함)
 ┃ ┣ 📜footer.html                          # 공통 푸터 템플릿
 ┃ ┗ 📜navbar.html                          # 공통 네비게이션 바 템플릿
 ┣ 📂users                                  # 사용자 관리와 관련된 앱 디렉토리
 ┃ ┣ 📂migrations                           # 데이터베이스 마이그레이션 파일 디렉토리
 ┃ ┃ ┣ 📜0001_initial.py                    # 초기 마이그레이션 파일
 ┃ ┃ ┗ 📜__init__.py                        # 마이그레이션 초기화 파일
 ┃ ┣ 📂templates                            # 사용자 앱 전용 템플릿 파일 디렉토리
 ┃ ┃ ┗ 📂users                              # 템플릿 세부 디렉토리
 ┃ ┃   ┣ 📜login.html                       # 사용자 로그인 페이지 템플릿
 ┃ ┃   ┣ 📜signup.html                      # 사용자 회원가입 페이지 템플릿
 ┃ ┃   ┗ 📜user_profile.html                # 사용자 프로필 페이지 템플릿
 ┃ ┣ 📜admin.py                             # 사용자 앱 관리자 페이지 설정
 ┃ ┣ 📜apps.py                              # 사용자 앱 설정 파일
 ┃ ┣ 📜forms.py                             # 사용자 관련 폼 정의
 ┃ ┣ 📜models.py                            # 사용자 및 관련 데이터베이스 모델 정의
 ┃ ┣ 📜tests.py                             # 사용자 앱 테스트 코드 작성
 ┃ ┣ 📜urls.py                              # 사용자 앱 URL 라우팅 설정
 ┃ ┣ 📜views.py                             # 사용자 관련 뷰 함수/클래스 정의
 ┃ ┗ 📜__init__.py                          # Python 패키지 초기화 파일
 ┣ 📜db.sqlite3                             # SQLite 데이터베이스 파일 (개발용)
 ┣ 📜manage.py                              # Django 명령어 실행 스크립트
 ┣ 📜README.md                              # 프로젝트 설명 문서
 ┗ 📜requirements.txt                       # 프로젝트 의존성 패키지 목록
``` 

### 디렉토리 및 파일 설명
1. `CH3_Assignment` (루트 디렉토리)
- Django 프로젝트의 최상위 디렉토리
- 주요 구성 파일(manage.py, README.md, requirements.txt, db.sqlite3)과 앱 디렉토리가 포함
2. `media/`
- github에는 제외되어 있지만, 업로드된 파일(예: 사용자 프로필 이미지, 게시물 첨부 파일)을 저장
- `default.png`: 기본 사용자 프로필 이미지
3. `my_pjt/`
- Django 프로젝트 설정 파일들이 위치한 디렉토리
- 주요 파일
  - `settings.py`: 프로젝트 전역 설정 (앱 목록, 데이터베이스, 미들웨어 등)
  - `urls.py`: 전역 URL 매핑 정의
  - `wsgi.py`, `asgi.py`: 배포 환경에서 서버 설정에 사용
4. `posts/`
- 게시물 관리와 관련된 앱 디렉토리
- 주요 디렉토리 및 파일
  - `migrations/`: 데이터베이스 구조 변경 기록
  - `templates/posts/`: 게시물과 관련된 HTML 템플릿
  - `models.py`: 게시물 및 좋아요, 댓글 모델 정의
  - `views.py`: 게시물 CRUD(생성, 읽기, 수정, 삭제) 로직
  - `forms.py`: 게시물 작성/수정 시 사용할 폼 정의
5. `static/`
- 정적 파일(CSS, JS, 이미지)을 저장
- 주요 디렉토리 및 파일:
  - `css/styles.css`: 프로젝트 전체에 적용되는 CSS 스타일 정의
6. `templates/`
- 프로젝트 전역에서 사용하는 공통 HTML 템플릿 디렉토리
- 주요 파일
  - `base.html`: 모든 템플릿이 상속받는 기본 레이아웃
  - `navbar.html`: 네비게이션 바 구성
  - `footer.html`: 푸터 구성
7. `users/`
- 사용자 인증 및 관리와 관련된 앱 디렉토리
- 주요 디렉토리 및 파일
  - `templates/users/`: 사용자 관련 HTML 템플릿(로그인, 회원가입, 프로필 페이지)
  - `models.py`: 사용자 모델 정의
  - `views.py`: 로그인, 회원가입, 프로필 관리 등 사용자 관련 로직
8. 주요 파일
- `db.sqlite3`: SQLite 데이터베이스 파일
- `manage.py`: Django 명령줄 도구를 실행하기 위한 스크립트
- `requirements.txt`: 프로젝트의 Python 패키지 의존성 목록



<br>

## 과제 내용
### ✅ User와 Post 앱 개발 (MTV 패턴)
### 1. User 앱

1. 사용자 모델 구현
    
    기본 Django User 모델을 확장하여 커스텀 필드 추가 (예: 프로필 이미지, 소개글)
    
    - `CustomUser`
2. 회원가입, 로그인, 로그아웃 기능 구현
    1. 회원가입
        - view: `signup` or `SignUpView`
        - template: `user/signup.html`
    2. 로그인
        - view: `login` or `LoginView`
        - template: `user/login.html`
    3. 로그아웃
        - view: `logout` or `LogoutView`
3. 사용자 프로필 페이지 구현
    - view: `user_profile` or `UserProfileView`
    - template: `user/profile.html`

### 2. Post 앱 (CRUD)

1. Post 모델 구현
    
    필드: 제목, 내용, 작성자, 작성일, 수정일
    
    - `Post`
2. 게시판 기능
    1. 게시글 목록 보기 (Read - List)
        - view: `post_list` or `PostListView`
        - template: `post/post_list.html`
    2. 게시글 상세 보기 (Read - Detail)
        - view: `post_detail` or `PostDetailView`
        - template: `post/post_detail.html`
    3. 게시글 작성 기능 (Create)
        - view: `post_create` or `PostCreateView`
        - template: `post/post_form.html`
    4. 게시글 수정 기능 (Update)
        - view: `post_update` or `PostUpdateView`
        - template: `post/post_form.html` (작성 기능과 공유)
    5. 게시글 삭제 기능 (Delete)
        - view: `post_delete` or `PostDeleteView`
        - template: `post/post_confirm_delete.html`

### ✅ 필수앱 구현 참고사항
**View**

- views.py는 함수 or 클래스 택 1

**기본 템플릿**

- 베이스 템플릿: `base.html`
- 네비게이션 바: `navbar.html`
- 푸터: `footer.html`

**데이터베이스**

- SQLite3

<br>

## 🔥도전 과제
### 1. 좋아요 기능

- Post 모델에 좋아요 필드 추가
- 좋아요 개수 표시

### 2. 댓글 기능

- Comment 모델 구현
    - `Comment`
- 댓글 기능
    - 댓글 작성
    - 댓글 수정
    - 댓글 삭제
- 게시글 상세 페이지에 댓글 목록 표시

<br>

## ✍️기능 확인
### users 앱
1. 사용자 모델 구현
    - 기본 Django User 모델을 확장하여 커스텀 필드 추가 (예: 프로필 이미지, 소개글)

        ```python
        from django.db import models
        from django.contrib.auth.models import AbstractUser

        class CustomUser(AbstractUser) :
            profile_img =models.ImageField(default='default.png',upload_to='images/')
            birth_date = models.DateField(null=True, blank=True)
            bio = models.TextField()
            address = models.CharField(max_length=50)
        ```

2. 회원가입, 로그인, 로그아웃 기능 구현
    1. 회원가입
        - view: `signup`

            ```python
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
            ```

        - template: [users/signup.html](https://github.com/hzi09/Assignment/blob/main/CH3_Assignment/users/templates/users/signup.html)
        - 구현 화면

           ![Image](https://github.com/user-attachments/assets/e47f34fa-a1f6-414f-85a7-fb17c519b902)

    2. 로그인
        - view: `login`
            ```python
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
            ```
        - template: [users/login.html](https://github.com/hzi09/Assignment/blob/main/CH3_Assignment/users/templates/users/login.html)
        - 구현 화면
            
            ![Image](https://github.com/user-attachments/assets/aa5186e1-b8ca-47c0-aa92-62012ebcd58c)

    3. 로그아웃
        - view: `logout`
            ```python
            @require_POST
            def logout(request):
                if request.method == "POST":
                    auth_logout(request)
                return redirect("posts:post_list")
            ```
        
3. 사용자 프로필 페이지 구현
    - view: `user_profile`
        ```python
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
                # 다른 사용자의 프로필에서는 form 표시하지 않기
                form = None

            context = {
                'form': form,
                'user': user,
                'is_owner': user == request.user, # 현재 로그인한 사용자가 해당 프로필의 소유자인지 여부
            }
            return render(request, 'users/user_profile.html', context)
        ```
    - template: [user/profile.html](https://github.com/hzi09/Assignment/blob/main/CH3_Assignment/users/templates/users/user_profile.html)
    - 화면 구현
      - 내 프로필을 들어갔을 때

        ![Image](https://github.com/user-attachments/assets/c891bb02-dd44-4876-8844-210a14fb1803)

      - 다른 사람의 프로필을 들어갔을 때(수정불가)

        ![Image](https://github.com/user-attachments/assets/f0ede3a0-8c99-4536-bf3d-6e498a3c0769)

<br>

### 2. Post 앱 (CRUD)

1. Post 모델 구현
    - 필드: 제목, 내용, 작성자, 작성일, 수정일
    ```python
        class Post(models.Model) :
        title = models.CharField(max_length=50)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')

        def __str__(self) :
            return self.title
    ```

2. 게시판 기능
    1. 게시글 목록 보기 (Read - List)
        - view: `post_list`
            ```python
            def post_list(request) :
                posts = Post.objects.all().order_by('-pk')
                context = {
                    "posts" : posts,
                }
                return render(request, 'posts/post_list.html', context)
            ```
        - template: [posts/post_list.html](https://github.com/hzi09/Assignment/blob/main/CH3_Assignment/posts/templates/posts/post_list.html)
        - 화면 구현
            
            ![Image](https://github.com/user-attachments/assets/69f08366-99d6-47e6-8401-9e8d2dd4ad7f)

    2. 게시글 상세 보기 (Read - Detail)
        - view: `post_detail`
            ```python
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
            ```
        - template: [posts/post_detail.html](https://github.com/hzi09/Assignment/blob/main/CH3_Assignment/posts/templates/posts/post_detail.html)
        - 화면 구현

            ![Image](https://github.com/user-attachments/assets/d85747b3-2f23-40c5-9cd3-4ab54c1ddc05)

    3. 게시글 작성 기능 (Create)
        - view: `post_create`
            ```python
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
            ```
        - template: [posts/post_form.html](https://github.com/hzi09/Assignment/blob/main/CH3_Assignment/posts/templates/posts/post_form.html)
        - 화면 구현

            ![Image](https://github.com/user-attachments/assets/39b1af5f-d780-4dd1-bbe5-fc97507236cf)

    4. 게시글 수정 기능 (Update)
        - view: `post_update`
            ```python
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
            ```
        - template(작성기능과 공유): [posts/post_form.html](https://github.com/hzi09/Assignment/blob/main/CH3_Assignment/posts/templates/posts/post_form.html)
        - 화면 구현

            ![Image](https://github.com/user-attachments/assets/47c65702-3f35-4cff-8fdd-c3a1dac79cf5)

    5. 게시글 삭제 기능 (Delete)
        - view: `post_delete`
            ```python
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
            ```
        - template: [posts/post_confirm_delete.html](https://github.com/hzi09/Assignment/blob/main/CH3_Assignment/posts/templates/posts/post_confirm_delete.html)
        - 화면 구현
            ![Image](https://github.com/user-attachments/assets/f47bd293-3ddc-4d2a-abaf-9691f90c4260)


### 3. 좋아요 기능
1.  Post 모델에 좋아요 필드 추가
    ```python
    class Post(models.Model) :
        # 생략

        like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_posts")

        def __str__(self) :
            return self.title
    ```
2. 좋아요 기능
   1. views : `like`
        ```python
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
        ```
    2. 화면 구현
        - 좋아요

            ![Image](https://github.com/user-attachments/assets/f6b480d6-eced-4cca-a6b8-f13c28ab67cf)

        - 좋아요 취소

            ![Image](https://github.com/user-attachments/assets/6f1c5960-b8d2-4d60-893c-02b1e6cf86aa)
    

### 4. 댓글 기능

1. Comment 모델 구현
    ```python
    class Comment(models.Model) :
        post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
        comment_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
        content = models.CharField(max_length=255)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self) :
            return self.content
    ````
2. 댓글 기능
    1. 댓글 작성 
      - views: `comment_create`
        ```python
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
        ```
      - 화면 구현
        
        ![Image](https://github.com/user-attachments/assets/a609c76c-6be2-491b-add1-063a6afcc724)
        
    2. 댓글 수정
      - views: `comment_update`
        ```python
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
        ```
      - 화면 구현

        ![Image](https://github.com/user-attachments/assets/caf332fe-1a2b-47e8-a81d-bd26acf8d723)

    3. 댓글 삭제
      - views: `comment_delete`
        ```python
        @require_POST
        def comment_delete(request, pk, comment_pk) :
            comment = get_object_or_404(Comment, pk=comment_pk)
            comment.delete()
            return redirect('posts:post_detail', pk=pk)
        ```

      - 화면 구현
        
        ![Image](https://github.com/user-attachments/assets/d56c90a9-83ad-48fd-9a4c-7f48f99c7cd0)

3. 게시글 상세 페이지에 댓글 목록 표시
   - 화면 구현

        ![Image](https://github.com/user-attachments/assets/9b7cb1df-7c79-4dac-80d3-b9bfddc246fb)