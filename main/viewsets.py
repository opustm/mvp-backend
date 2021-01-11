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

class DirectMessageViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset= models.DirectMessage.objects.all()
    serializer_class = serializers.DirectMessageSerializer

class CliqueMessageViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset= models.CliqueMessage.objects.all()
    serializer_class = serializers.CliqueMessageSerializer

class ReactionViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset= models.Reaction.objects.all()
    serializer_class = serializers.ReactionSerializer

class ToDoViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset= models.ToDo.objects.all()
    serializer_class = serializers.ToDoSerializer

class RequestViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset= models.Request.objects.all()
    serializer_class = serializers.RequestSerializer