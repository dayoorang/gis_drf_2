from django.contrib.auth.models import User
from rest_framework import serializers


class NewModelSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data): # 비번 암호화 과정 위해서 사용
        user = User.objects.create_user(**validated_data)
        return user


class UserWithoutPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','date_joined']



