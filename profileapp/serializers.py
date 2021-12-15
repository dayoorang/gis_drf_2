from rest_framework import serializers

from accountapp.serializers import UserWithoutPasswordSerializer
from profileapp.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = UserWithoutPasswordSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['id','nickname','image','message','owner']