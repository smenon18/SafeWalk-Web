from rest_framework import serializers
from api.models import User, ParentalRel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'password', 'email')

class ParentalRelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentalRel
        fields = ('id','child', 'parent')
