from rest_framework import serializers
from api.models import User, ParentalRel, InTransit

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'password', 'email')

class ParentalRelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentalRel
        fields = ('id','child', 'parent')

class InTransitSerializer(serializers.ModelSerializer):
    class Meta:
        model = InTransit
        fields = ('id','child','depart_time','expected_arrival_time','has_arrived','est_distance','start_pos', 'end_pos')
