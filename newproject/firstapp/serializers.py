from rest_framework import serializers

from .models import Name, AcitvityPeriod

class NameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Name
        fields = ['name']

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    name = NameSerializer()
    class Meta:
        model = AcitvityPeriod
        fields = ['name' ,'data']