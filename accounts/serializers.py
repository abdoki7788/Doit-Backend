from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "nickname", "email"]
        read_only_fields = ["id", "email"]


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = ["nickname", "email", "password", "password2"]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password2": "دو رمز عبور مطابقت نداشتند"})
        return super().validate(attrs)

    def get_cleaned_data(self):
        return {
            "nickname": self.validated_data.get("nickname", ""),
            "password": self.validated_data.get("password1", ""),
            "email": self.validated_data.get("email", ""),
        }
    
    def create(self, validated_data):
        user = get_user_model().objects.create(
            nickname=validated_data["nickname"],
            email=validated_data["email"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
