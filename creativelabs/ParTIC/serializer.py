from rest_framework import serializers
from models import Party

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ('name', 'address','status','distance',
        'entryFee','datetime','guysAllowed')
