from rest_framework import serializers
from events.models import Event, EventPlace
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

    places = EventPlaceSerializer(many=True)

    class Meta:
        model = Event
        fields = ["id", "event", "description", "user", "places"]
        read_only_fields = ['id']

    def create(self, validated_data):
        places_obj_list = []
        for place in validated_data.pop('places'):
            places_obj_list.append(
                EventPlace.objects.get_or_create(
                    city=place['city'],
                    event_time=place['event_time']
                )
            )
        event = Event.objects.create(**validated_data)
        event.places.add(places_obj_list)
        return event


