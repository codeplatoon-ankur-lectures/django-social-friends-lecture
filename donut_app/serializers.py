from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["id", "username", "password", "friends"]

    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        # extract "extra data"
        username = validated_data.pop("username")
        password = validated_data.pop("password")

        # create base user
        new_user = User.objects.create_user(username=username, password=password)
        
        # associate new user with the user profile
        validated_data["user"] = new_user

        # create the actual user profile
        return super().create(validated_data)


class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ["id", "sender", "receiver", "accepted"]

    def validate(self, attrs):
        if "sender" in attrs and "receiver" in attrs:
            instance = FriendRequest(sender=attrs["sender"], receiver=attrs["receiver"])
            try:
                instance.full_clean()
            except ValidationError as ve:
                raise serializers.ValidationError(ve)

        return super().validate(attrs)


    




    