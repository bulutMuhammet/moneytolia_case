from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def validate(self, attr):
        validate_password(attr["password"])
        return attr

    def validate_email(self, email):
        email = email.lower()
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                'This email is already registered')
        return email

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"]
        )
        user.set_password(validated_data["password"])
        user.save()

        return user


