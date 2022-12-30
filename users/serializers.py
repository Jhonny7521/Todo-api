from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError
from django.contrib.auth import get_user_model
from .models import User


class SignUpSerializer(serializers.ModelSerializer):
  first_name = serializers.CharField(max_length=50)
  last_name = serializers.CharField(max_length=50)
  email = serializers.CharField(max_length=80)
  username = serializers.CharField(max_length=45)
  password = serializers.CharField(min_length=8, write_only=True)

  class Meta:
    model = User
    fields = ["first_name", "last_name", "email", "username", "password"]

  def validate(self, attrs):
    email_exists = User.objects.filter(email=attrs["email"]).exists()
    if email_exists:
      raise ValidationError("El email ya ha sido usado")

    return super().validate(attrs)

  def create(self, validated_data):
    password = validated_data.pop("password")
    user = super().create(validated_data)
    user.set_password(password)
    user.save()
    Token.objects.create(user=user)

    return user


class SignUpAdminSerializer(serializers.ModelSerializer):
  email = serializers.CharField(max_length=80)
  username = serializers.CharField(max_length=45)
  password = serializers.CharField(min_length=8, write_only=True)

  class Meta:
    model = User
    fields = ["email", "username", "password"]

  def validate(self, attrs):
    email_exists = User.objects.filter(email=attrs["email"]).exists()
    if email_exists:
      raise ValidationError("El email ya ha sido usado")

    return super().validate(attrs)

  def create(self, validated_data):
    print(validated_data)
    user = get_user_model()
    new_user = user.objects.create_superuser(**validated_data)
    print(new_user)
    Token.objects.create(user=new_user)

    return user


class GetUserSerializer(serializers.ModelSerializer):
  email = serializers.CharField(max_length=80)
  username = serializers.CharField(max_length=45)
  password = serializers.CharField(min_length=8, write_only=True)

  class Meta:
    model = User
    fields = ["email", "username", "password"]    