from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.PostListAPIView.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetailAPIView.as_view(), name='post_detail'),
    path('<int:pk>/like/', views.LikeAPIView.as_view(), name='like'),
    path('<int:pk>/comment/', views.CommentAPIView.as_view(), name='comment_create'),
    path('<int:pk>/comment/<int:comment_pk>/', views.CommentUDAPIView.as_view(), name='comment_ud')
]