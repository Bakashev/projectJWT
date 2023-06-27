from rest_framework import serializers
from events.models import Events, EventPlace
from django.contrib.auth.models import User


class UserSeializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "is_staff", "password"]
        #read_only_fields = ['username']

class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]
        read_only_fields = ['username']
class EventPlaceSerializer(serializers.ModelSerializer):
    #user = UserSeializer(many=True)
    class Meta:
        model = EventPlace
        fields = ['city', 'event_time']

class EventSerializer(serializers.ModelSerializer):
    user = UserNameSerializer(many=True, read_only=True)

    place = EventPlaceSerializer(many=True)

    class Meta:
        model = Events
        fields = ["id", "event", "user", "place"]
        read_only_fields = ['id']



