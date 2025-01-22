from rest_framework import serializers
from .models import CustomUser


class CustomUserCreationSerializer(serializers.ModelSerializer) :
    # 비밀번호는 응답 데이터에 포함되지 않도록 함
    password = serializers.CharField(write_only=True)

    class Meta :
        model = CustomUser
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        """
        - validated_data: 사용자로부터 받은 데이터를 검증 후 전달받은 딕셔너리
        - username, email, password를 받아 CustomUser 객체를 생성
        - Django의 create_user 메서드를 사용하여 비밀번호가 해싱된 상태로 저장
        """
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user # 생성된 사용자 객체 반환
    

class CustomUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'profile_img', 'birth_date', 'bio', 'address']