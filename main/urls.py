from django.urls import path, include
from .views import current_user, index, team, UserDetails, TeamDetails, CliqueDetails, TeamEvents, UserSoloEvents, InvitationDetails, TeamMembers, CliqueMembers, UserScheduleTimeFrames, TeamAnnouncements

urlpatterns = [
    path('', index),
    path('current_user/', current_user),
    path('userDetails/<str:username>/', UserDetails.as_view()),
    path('teamDetails/<str:name>/', TeamDetails.as_view()),
    path('teamMembers/<str:name>/', TeamMembers.as_view()),
    path('cliqueDetails/<str:name>/', CliqueDetails.as_view()),
    path('cliqueMembers/<str:name>/', CliqueMembers.as_view()),    
    path('invitationDetails/<str:code>/', InvitationDetails.as_view()),
    path('teamEvents/<str:name>/', TeamEvents.as_view()),
    path('userSoloEvents/<str:username>/', UserSoloEvents.as_view()),
    path('userScheduleTimeFrames/<str:username>/', UserScheduleTimeFrames.as_view()),
    path('teamAnnouncements/<str:name>/', TeamAnnouncements.as_view())
]