from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import permissions, status

class CliqueViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset= models.Clique.objects.all()
    serializer_class = serializers.CliqueSerializer
    
class UserViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset= models.User.objects.all()
    serializer_class = serializers.UserSerializer

class InvitationViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset= models.Invitation.objects.all()
    serializer_class = serializers.InvitationSerializer

class EventViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset= models.Event.objects.all()
    serializer_class = serializers.EventSerializer

class SoloEventViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset= models.SoloEvent.objects.all()
    serializer_class = serializers.SoloEventSerializer

class ScheduleViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset= models.Schedule.objects.all()
    serializer_class = serializers.ScheduleSerializer

class TimeFrameViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset= models.TimeFrame.objects.all()
    serializer_class = serializers.TimeFrameSerializer

class AnnouncementViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset= models.Announcement.objects.all()
    serializer_class = serializers.AnnouncementSerializer
