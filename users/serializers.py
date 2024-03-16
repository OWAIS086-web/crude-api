from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ['user', 'city', 'cnic', 'address']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_instance = User.objects.create(**user_data)
        user_profile_instance = UserProfile.objects.create(user=user_instance, **validated_data)
        return user_profile_instance

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)

        if user_data:
            user_instance = instance.user
            user_instance.username = user_data.get('username', user_instance.username)
            user_instance.email = user_data.get('email', user_instance.email)
            user_instance.first_name = user_data.get('first_name', user_instance.first_name)
            user_instance.last_name = user_data.get('last_name', user_instance.last_name)
            user_instance.save()

        instance.city = validated_data.get('city', instance.city)
        instance.cnic = validated_data.get('cnic', instance.cnic)
        instance.address = validated_data.get('address', instance.address)
        instance.save()

        return instance

    def delete(self, instance):
        instance.user.delete()
        instance.delete()


""""
1. first 3 line we import serializer from rest_framework then,
   User from auth, UserProfile from model.py file

2. first serilizer is create for user which is link with over user model 
   second serilizer  is  create for profile which is link with user profile model 

3. I add username from my side to avoide error when trying to create a new user 
   without providing a unique username.

4. use instance of filed to update and delete 
"""
