from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import permissions, status

class TeamViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset= models.Team.objects.all()
    serializer_class = serializers.TeamSerializer
    
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

class WeekScheduleViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset= models.WeekSchedule.objects.all()
    serializer_class = serializers.WeekScheduleSerializer