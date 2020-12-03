
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.middleware.csrf import get_token
from django.http import Http404

from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import Event, Invitation, User, Team
from .serializers import TeamSerializer, UserSerializer, InvitationSerializer, EventSerializer, UserSerializerWithToken



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

    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return False

    def get(self, request, username, format=None):
        user = self.get_object(username)
        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, username, format=None):
        inv = self.get_object(username)
        serializer = InvitationSerializer(inv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username, format=None):
        inv = self.get_object(username)
        inv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''-------------------------------------------------------------------------'''

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
        allTeams = Team.objects.all()
        serializer = TeamSerializer(allTeams, many=True)
        return Response(serializer.data)

class TeamDetail(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, name):
        try:
            return Team.objects.get(name=name)
        except Team.DoesNotExist:
            return False

    def get(self, request, name, format=None):
        team = self.get_object(name)
        if team:
            serializer = TeamSerializer(team)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, name, format=None):
        inv = self.get_object(name)
        serializer = InvitationSerializer(inv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name, format=None):
        inv = self.get_object(name)
        inv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TeamMembersByTeamId(APIView):

    def get(self, request, teamid, format=None):
        userQuerySet=User.objects.values('username', 'teams')
        members=[]
        for user in userQuerySet:
            if user["teams"]==teamid:
                members.append(user["username"])
        return Response(members, status=status.HTTP_200_OK)

class TeamMembersByTeamName(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, name, format=None):
        teamQuerySet = Team.objects.values('id', 'name')
        for team in teamQuerySet:
            if team['name']==name:
                teamid=team['id']
        if teamid:
            userQuerySet=User.objects.values('username', 'teams')
            members=[]
            for user in userQuerySet:
                if user["teams"]==teamid:
                    members.append(user["username"])
            return Response(members, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

'''--------------------------------------------------------------------------------'''

class InvitationList(APIView):
    """
    Create new invitation. Get all invitations.
    """

    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        allInvitations = Invitation.objects.all()
        serializer = InvitationSerializer(allInvitations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InvitationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InvitationDetail(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, code):
        try:
            return Invitation.objects.get(code=code)
        except Invitation.DoesNotExist:
            return False

    def get(self, request, code, format=None):
        inv = self.get_object(code)
        if inv:
            serializer = InvitationSerializer(inv)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, code, format=None):
        inv = self.get_object(code)
        serializer = InvitationSerializer(inv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, code, format=None):
        inv = self.get_object(code)
        inv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''------------------------------------------------------------------------------------------'''

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

class EventDetail(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return False

    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        if event:
            serializer = EventSerializer(event)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





'''-------------------------------------------------------------------------------------------------------------'''





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
