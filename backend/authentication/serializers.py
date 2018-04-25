from rest_framework import serializers
from .models import User, ROLES, ADMIN_ROLES


class UserSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  username = serializers.CharField(required=False, allow_blank=False, max_length=30)
  email = serializers.CharField(required=False, allow_blank=True)
  first_name = serializers.CharField(required=False, allow_blank=True, max_length=30)
  last_name = serializers.CharField(required=False, allow_blank=True, max_length=30)
  role = serializers.ChoiceField(choices=ROLES, default='user')
  password = serializers.CharField(write_only=True, min_length=5)
  birth_date = serializers.DateTimeField(required=False)
  phone = serializers.CharField(max_length=30, allow_blank=False)
  city = serializers.CharField(max_length=30, allow_blank=False)

  def create(self, validated_data):
    user = User( ** validated_data)
    user.set_password(validated_data['password'])
    user.save()
    return user

  def update(self, user, validated_data):
    user.__dict__.update( ** validated_data)
    if 'password' in validated_data:
      user.set_password(validated_data['password'])
    user.save()
    return user

class AdminSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  username = serializers.CharField(required=False, allow_blank=False, max_length=30)
  password = serializers.CharField(write_only=True, min_length=5)
  email = serializers.CharField(required=True, allow_blank=False)
  role = serializers.ChoiceField(required=True, choices=ADMIN_ROLES)

  def create(self, validated_data):
    user = User( ** validated_data)
    user.set_password(validated_data['password'])
    user.save()
    return user

  def update(self, user, validated_data):
    user.__dict__.update( ** validated_data)
    if 'password' in validated_data:
      user.set_password(validated_data['password'])
    user.save()
    return user
