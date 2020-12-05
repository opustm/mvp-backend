from django.urls import path, include
from .views import current_user, index, team, UserDetail, TeamDetail, EventsByTeamname, UserEventsByUsername, InvitationDetail, TeamMembersByTeamname, ScheduleTimeFramesByUsername, AnnouncementsByTeamName

urlpatterns = [
    path('', index),
    path('current_user/', current_user),
    path('userByUsername/<str:username>/', UserDetail.as_view()),
    path('teamByTeamname/<str:name>/', TeamDetail.as_view()),
    path('teamMembers/<str:name>/', TeamMembersByTeamname.as_view()),
    path('invitationByCode/<str:code>/', InvitationDetail.as_view()),
    path('teamEventsByTeamname/<str:name>/', EventsByTeamname.as_view()),
    path('userEventsByUsername/<str:username>/', UserEventsByUsername.as_view()),
    path('usersScheduleTimeFramesByUsername/<str:username>/', ScheduleTimeFramesByUsername.as_view()),
    path('teamAnnouncementsByUsername/<str:name>/', AnnouncementsByTeamName.as_view())
]