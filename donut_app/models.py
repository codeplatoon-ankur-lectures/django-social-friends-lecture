from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.forms import ValidationError


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    friends = models.ManyToManyField("self", blank=True)
    # friend_requests_sent
    # friend_requests_received

    def __str__(self):
        return f"USER PROFILE: {self.user.username} has {len(self.friends.all())} friends"


class FriendRequest(models.Model):
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="friend_requests_sent")
    receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="friend_requests_received")
    accepted = models.BooleanField(default=False)

    def clean(self):
        if self.sender == self.receiver:
            raise ValidationError("You can't be friends with yourself")

        return super().clean()

    def __str__(self):
        return f"FRIEND REQUEST: {self.sender.username} sent a friend request to {self.receiver.username}"


class FriendGroup(models.Model):
    name = models.CharField(max_length=64)
    members = models.ManyToManyField(UserProfile, related_name="groups")

    def __str__(self):
        return f"FRIEND GROUP: {self.name}"


