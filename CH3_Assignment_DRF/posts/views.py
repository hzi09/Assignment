from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import PostForm, CommentForm
from .models import Post, Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer, CommentSerializer

def home(request) :
    return render(request, 'posts/home.html')


class PostListAPIView(APIView) :
    permission_classes = [IsAuthenticated]

    def get(self, request) :
        posts = Post.objects.all().order_by('-pk')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
        
    def post(self, request) :
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostDetailAPIView(APIView) :
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Post, pk=pk)

    def get(self, request, pk) :
        post = self.get_object(pk)
        comments = post.comments.all().order_by('-pk')

        edit_comment = request.GET.get('edit_comment')
        try:
            edit_comment = int(edit_comment) if edit_comment else None
        except ValueError:
            edit_comment = None
        
        post_serializer = PostSerializer(post)
        comment_serializer = CommentSerializer(comments, many=True)

        # 응답 데이터 구성
        response_data = {
            "post": post_serializer.data,
            "comments": comment_serializer.data,
            "edit_comment": edit_comment,
        }

        return Response(response_data)

    def put(self, request, pk) :
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, request, pk) :
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LikeAPIView(APIView) :
    permission_classes = [IsAuthenticated]


    '''
    좋아요 기능
    '''
    def post(self, request, pk) :

        post = get_object_or_404(Post, pk=pk)
        
        if post.like_users.filter(pk=request.user.pk).exists():
            post.like_users.remove(request.user)
            response_data = {
                "message": "Like removed", 
                "likes_count": post.like_users.count()
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else :
            post.like_users.add(request.user)
            response_data = {
                "message": "Liked", 
                "likes_count": post.like_users.count()
            }
            return Response(response_data, status=status.HTTP_200_OK)


class CommentAPIView(APIView) :
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        '''
        댓글 생성
        '''
        post = get_object_or_404(Post, pk=pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid() :
            comment = serializer.save(post=post, comment_user=request.user)
            response_data = {
                "message": "Comment created",
                "comment": CommentSerializer(comment).data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        # 유효성 검사에 실패하면 serializer.errors에 오류 정보 저장
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentUDAPIView(APIView) :

    def put(self, request, pk, comment_pk) :
        '''
        댓글 수정
        '''
        comment = get_object_or_404(Comment, pk=comment_pk, comment_user=request.user)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid() :
            update_comment = serializer.save()
            response_data = {
                "message": "Comment updated", 
                "comment": CommentSerializer(update_comment).data,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, comment_pk) :
        '''
        댓글 삭제
        '''
        comment = get_object_or_404(Comment, pk=comment_pk, comment_user=request.user)
        comment.delete()
        response_data = {
                "message": "Comment deleted", 
            }
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)