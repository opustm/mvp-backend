from django.urls import path, include
from .views import current_user, UserList, index, team, UserDetail, TeamList, TeamDetail, EventList, EventDetail, EventsByTeamname, UserEventList, UserEventDetail, UserEventsByUsername, InvitationList, InvitationDetail, TeamMembersByTeamname, ScheduleTimeFrameList, ScheduleTimeFramesByUsername, AnnouncementsByTeamName

urlpatterns = [
    path('', index),
    path('current_user/', current_user),
    path('user/<str:username>/', UserDetail.as_view()),
    path('team/<str:name>/', TeamDetail.as_view()),
    path('teamMembers/<str:name>/', TeamMembersByTeamname.as_view()),
    path('invitation/<str:code>/', InvitationDetail.as_view()),
    path('eventsByTeamName/<str:name>/', EventsByTeamname.as_view()),
    path('userEventsByUsername/<str:username>/', UserEventsByUsername.as_view()),
    path('scheduleTimeFramesByUsername/<str:username>/', ScheduleTimeFramesByUsername.as_view()),
    path('announcementsByTeamName/<str:name>/', AnnouncementsByTeamName.as_view())
    

]