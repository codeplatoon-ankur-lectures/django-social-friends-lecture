from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class FriendRequestViewSet(viewsets.ModelViewSet):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    def perform_update(self, serializer):
        # if accepted = True
        #   add friend to both User Profiles
        #   delete our friend request
        updated_friend_request = serializer.instance
        if updated_friend_request.accepted == True:
            sender = UserProfile.objects.get(pk=updated_friend_request.sender.id)
            receiver = UserProfile.objects.get(pk=updated_friend_request.receiver.id)


            print("///////////////// adding new friends!")
            sender.friends.add(receiver)
            receiver.friends.add(sender)

            sender.save()
            receiver.save()

            return self.destroy(self.request)

        return serializer.save()



# serializer
## instance ... the python object, model record
## data ... the "json" representation