from urllib import request

from rest_framework.response import Response
from rest_framework import generics, permissions
from .serializaers import EventSerializer, EventPlaceSerializer, UserSeializer
from ..models import Events, EventPlace
from django.contrib.auth.models import User
import datetime
from .permissions import IsAdminUserOrCreateOnly


class EventApiViews(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Events.objects.filter(place__event_time__gt=datetime.datetime.now())

    def perform_create(self, serializer):
        serializer.save(user=request.user)



class ListUsersAPIViews(generics.ListCreateAPIView):
    serializer_class = UserSeializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUserOrCreateOnly]


class ParticipateAPIEvent(generics.RetrieveUpdateAPIView):
    serializer_class = EventSerializer
    queryset = Events.objects.filter(place__event_time__gt=datetime.datetime.now())
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'











