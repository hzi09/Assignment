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
 ┃ ┣ 📜serializers.py                       # DRF 직렬화 정의 파일
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
 ┃ ┣ 📜serializers.py                       # DRF 직렬화 정의 파일
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
  - `serializers.py`: DRF 직렬화 정의 파일
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
  - `serializers.py`: DRF 직렬화 정의 파일
  - `views.py`: 로그인, 회원가입, 프로필 관리 등 사용자 관련 로직
8. 주요 파일
- `db.sqlite3`: SQLite 데이터베이스 파일
- `manage.py`: Django 명령줄 도구를 실행하기 위한 스크립트
- `requirements.txt`: 프로젝트의 Python 패키지 의존성 목록



<br>

## 🔥도전 과제
### 1. DRF(Django Rest Framework)로 변환

- User와 Post 앱을 API로 변환
- Serializer 구현
    - `UserSerializer`
    - `PostSerializer`
- APIView 사용하여 CRUD 기능 구현
- URL 설정 및 라우팅

### 2. 데이터베이스
- SQLite3에서 PostgreSQL or MySQL로 마이그레이션

## ✍️기능 확인
### posts 앱
- posts 앱 : code 바로가기
  - [serializers.py](https://github.com/hzi09/Assignment/blob/main/CH3_Assignment_DRF/posts/serializers.py)
  - [views.py](https://github.com/hzi09/Assignment/blob/main/CH3_Assignment_DRF/posts/views.py)
  - [urls.py](https://github.com/hzi09/Assignment/blob/main/CH3_Assignment_DRF/posts/urls.py)

#### PostListAPIView
- 게시글 목록보기(`GET`)
  
![Image](https://github.com/user-attachments/assets/91425f49-dbdd-4c5c-b128-10f45fd57dda)

#### PostDetailAPIView
- 게시글 상세조회(`GET`)

![Image](https://github.com/user-attachments/assets/03e9e72b-b131-486b-a029-4a77be326c54)

- 게시글 생성(`POST`)

![Image](https://github.com/user-attachments/assets/32ec751f-495e-4e51-8cfa-828ea3fb7ce2)

- 게시글 수정(`PUT`)

![Image](https://github.com/user-attachments/assets/bf405d6d-5e75-4689-bd15-120c64c78685)



#### LikeAPIView
- 인증되지 않은 사용자

![Image](https://github.com/user-attachments/assets/585718d5-0ac7-4036-942c-3d9d02eac866)

- 좋아요/좋아요 취소(`POST`)

![Image](https://github.com/user-attachments/assets/0b03f263-8b16-4142-b00a-18d7bfe1bf11)

![Image](https://github.com/user-attachments/assets/9da2b9a9-b847-437c-9381-22d69fb6132b)


#### CommentAPIView

- 댓글 생성(`POST`)

![Image](https://github.com/user-attachments/assets/f24a0c32-be30-4b25-8b96-fe74a47b6a78)


#### CommentUDAPIView
- 수정과 삭제는 comment_pk가 필요하기 때문에 url 분리함
- 댓글 수정(`PUT`)

![Image](https://github.com/user-attachments/assets/68f032f2-2d62-4729-967c-57725ddfdd3e)

- 댓글 삭제(`DELETE`)

![Image](https://github.com/user-attachments/assets/752973ef-0710-4ffb-9df2-c5234c95268f)

<br>

### users 앱
- users 앱 : code 바로가기
  - [serializers.py](https://github.com/hzi09/Assignment/blob/main/CH3_Assignment_DRF/users/serializers.py)
  - [views.py](https://github.com/hzi09/Assignment/blob/main/CH3_Assignment_DRF/users/views.py)
  - [urls.py](https://github.com/hzi09/Assignment/blob/main/CH3_Assignment_DRF/users/urls.py)

#### SignupAPIView

![Image](https://github.com/user-attachments/assets/62614464-ddd2-4964-89ad-e21e8b291e68)


#### Login

![Image](https://github.com/user-attachments/assets/f740a448-bc4d-4b61-ba5e-7d24a53cf421)


#### Refresh Token

![Image](https://github.com/user-attachments/assets/931f2f3a-e4c3-44c6-b88a-89143c83813c)


#### LogoutAPIView

![Image](https://github.com/user-attachments/assets/1f194713-1175-42f4-a7fb-e192d40ed931)


#### UserProfileAPIView

- 보기(`GET`)

![Image](https://github.com/user-attachments/assets/cd478271-a4c3-40a7-8473-73864e886bfd)

- 수정(`PUT`)

![Image](https://github.com/user-attachments/assets/687763ff-bcf0-4945-9a9c-5b02356f1362)


### DB(SQLite3 → MySQL)
    
- Django 데이터베이스 설정 변경

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db',
        'USER' : 'root',
        'PASSWORD' : '1234',
        'HOST' : 'localhost',
        'PORT' : '3306',
        'OPTIONS': {
            # MySQL의 데이터 무결성을 보장
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            # 이모지 및 다양한 유니코드 문자를 저장할 수 있도록 보장
            'charset': 'utf8mb4', 
            # Django와 MySQL 간 유니코드 데이터 처리를 원활하게 함
            'use_unicode': True,
        },
    }
}
```
- MySQL에서 DB 테이블 확인

![Image](https://github.com/user-attachments/assets/08ce9d82-9c48-4976-97c0-48cd1b9e4eb4)