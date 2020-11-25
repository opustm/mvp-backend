
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.middleware.csrf import get_token
from django.http import Http404

from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Event, Invitation, User, Team
from .serializers import TeamSerializer, UserSerializer, InvitationSerializer, EventSerializer, UserSerializerWithToken

def index(request):
    return HttpResponse("Welcome to the OPUS-TM API")

def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})

def ping(request):
    return JsonResponse({'result': 'OK'})

@api_view(['GET'])
def team(request):
    serializer=TeamSerializer(request.team)
    return Response(serializer.data)

@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. Get all Users.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        allUsers = User.objects.all()
        serializer = UserSerializer(allUsers, many=True)
        return Response(serializer.data)


class UserDetail(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return False

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)


class TeamList(APIView):
    """
    Create a new team. Get all teams.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        allUsers = Team.objects.all()
        serializer = TeamSerializer(allUsers, many=True)
        return Response(serializer.data)

class EventList(APIView):
    """
    Create a new Event. Get all Events.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        allEvents = Event.objects.all()
        serializer = EventSerializer(allEvents, many=True)
        return Response(serializer.data)

class InvitationList(APIView):
    """
    Create a new team. Get all teams.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = InvitationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        allInvitations = Invitation.objects.all()
        serializer = InvitationSerializer(allInvitations, many=True)
        return Response(serializer.data)

class TeamDetail(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, pk):
        try:
            return Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            return False

    def get(self, request, pk, format=None):
        team = self.get_object(pk)
        if team:
            serializer = TeamSerializer(team)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
