from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, min_length=8)

    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'email', 'role', 'is_active', 'is_staff', 'password']
        read_only_fields = ['id', 'is_active', 'is_staff']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            # Prevent normal users from changing role here if you want
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
