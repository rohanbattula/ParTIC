
from rest_framework import serializers
from party.models import Party

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ('name', 'address','status','distance',
        'entryFee','dateTime','guysAllowed', 'createdBy')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','age','email','profilePic')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user','image')
