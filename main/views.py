
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.middleware.csrf import get_token
from django.http import Http404

from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import Event, Invitation, User, UserEvent, Team, ScheduleTimeFrame, Announcement
from .serializers import TeamSerializer, UserSerializer, AnnouncementSerializer, InvitationSerializer, EventSerializer, UserEventSerializer, UserSerializerWithToken, ScheduleTimeFrameSerializer



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
        team = self.get_object(name)
        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name, format=None):
        team = self.get_object(name)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#WE ALREADY HAVE THIS ONE WITH DEFAULT VIEWSET:
class TeamMembersByTeamId(APIView):
    def get(self, request, teamid, format=None):
        userQuerySet=User.objects.values('username', 'teams')
        members=[]
        for user in userQuerySet:
            if user["teams"]==teamid:
                members.append(user["username"])
        return Response(members, status=status.HTTP_200_OK)

class TeamMembersByTeamname(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except Team.DoesNotExist:
            return False
    def get(self, request, name, format=None):
        teamQuerySet = Team.objects.values('id', 'name')
        teamid=None
        for team in teamQuerySet:
            if team['name']==name:
                teamid=team['id']
        if teamid:
            userQuerySet=User.objects.values('username', 'teams')
            members=[]
            for user in userQuerySet:
                if user["teams"]==teamid:
                    members.append(UserSerializer(self.get_object(user['username'])).data)
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

class EventsByTeamname(APIView):
    permission_classes = (permissions.AllowAny,)
    def get_object(self, eventid):
        try:
            return Event.objects.get(id=eventid)
        except Event.DoesNotExist:
            return False

    def get(self, request, name, format=None):
        teamQuerySet = Team.objects.values('id', 'name')
        teamid=None
        for team in teamQuerySet:
            if team['name']==name:
                teamid=team['id']
        if teamid:
            eventQuerySet=Event.objects.values('id', 'team')
            events=[]
            for event in eventQuerySet:
                if event["team"]==teamid:
                    events.append(EventSerializer(self.get_object(event['id'])).data)
            return Response(events, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

'''------------------------------------------------------------------------------------------'''

class UserEventList(APIView):
    """
    Create a new UserEvent. Get all UserEvents.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserEventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        allUserEvents = UserEvent.objects.all()
        serializer = UserEventSerializer(allUserEvents, many=True)
        return Response(serializer.data)

class UserEventDetail(APIView):
    permission_classes = (permissions.AllowAny,)

    def get_object(self, pk):
        try:
            return UserEvent.objects.get(pk=pk)
        except UserEvent.DoesNotExist:
            return False

    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        if event:
            serializer = UserEventSerializer(event)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = UserEventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserEventsByUsername(APIView):
    permission_classes = (permissions.AllowAny,)
    def get_object(self, eventid):
        try:
            return UserEvent.objects.get(id=eventid)
        except UserEvent.DoesNotExist:
            return False

    def get(self, request, username, format=None):
        userQuerySet = User.objects.values('id', 'username')
        userid=None
        for user in userQuerySet:
            if user['username']==username:
                userid=user['id']
        if userid:
            eventQuerySet=UserEvent.objects.values('id', 'user')
            events=[]
            for event in eventQuerySet:
                if event["user"]==userid:
                    events.append(UserEventSerializer(self.get_object(event['id'])).data)
            return Response(events, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

'''-------------------------------------------------------------------------'''
class ScheduleTimeFrameList(APIView):
    """
    Create a new Schedule. Get all Schedules.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = ScheduleTimeFrameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        allScheduleTimeFrames = ScheduleTimeFrame.objects.all()
        serializer = ScheduleTimeFrameSerializer(allScheduleTimeFrames, many=True)
        return Response(serializer.data)

class ScheduleTimeFramesByUsername(APIView):
    permission_classes = (permissions.AllowAny,)
    def get_object(self, scheduleid):
        try:
            return ScheduleTimeFrame.objects.get(id=scheduleid)
        except ScheduleTimeFrame.DoesNotExist:
            return False

    def get(self, request, username, format=None):
        userQuerySet = User.objects.values('id', 'username')
        userid=None
        for user in userQuerySet:
            if user['username']==username:
                userid=user['id']
        if userid:
            scheduleTimeFrameQuerySet = ScheduleTimeFrame.objects.values('user', 'id')
            idsOfUsersSchedules=[]
            for schedule in scheduleTimeFrameQuerySet:
                if schedule['user']==userid:
                    idsOfUsersSchedules.append(schedule['id'])
            if idsOfUsersSchedules:
                schedules=[]
                for scheduleid in idsOfUsersSchedules:
                    schedules.append(ScheduleTimeFrameSerializer(self.get_object(scheduleid)).data)
                if schedules:
                    return Response(schedules, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

'''-----------------------------------------------------------------------------------------------------------'''   

class AnnouncementsByTeamName(APIView):
    permission_classes = (permissions.AllowAny,)
    def get_object(self, announcementid):
        try:
            return Announcement.objects.get(id=announcementid)
        except Announcement.DoesNotExist:
            return False

    def get(self, request, name, format=None):
        teamQuerySet = Team.objects.values('id', 'name')
        teamid=None
        for team in teamQuerySet:
            if team['name']==name:
                teamid=team['id']
        if teamid:
            announcementQuerySet=Announcement.objects.values('id', 'team')
            announcements=[]
            for announcement in announcementQuerySet:
                if announcement["team"]==teamid:
                    announcements.append(AnnouncementSerializer(self.get_object(announcement['id'])).data)
            return Response(announcements, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


'''-------------------------------------------------------------------------------------------------------------'''





def index(request):
    return HttpResponse("Welcome to the OPUS-TM API")

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
