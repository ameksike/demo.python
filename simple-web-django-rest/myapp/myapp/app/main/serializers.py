from .models import *
from rest_framework import serializers

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('firstName', 'lastName', 'age', 'sex', 'born')