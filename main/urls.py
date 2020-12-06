from django.urls import path, include
from .views import current_user, UserList, index, team, UserDetails, TeamDetails, CliqueDetails, CliqueEvents, UserSoloEvents, InvitationDetails, TeamMembers, CliqueMembers, UserSchedules, ScheduleTimeFrames, CliqueAnnouncements

urlpatterns = [
    path('', index),
    path('current_user/', current_user),
    # path('users/', UserList.as_view()),
    path('userDetails/<str:username>/', UserDetails.as_view()),
    path('teamDetails/<str:name>/', TeamDetails.as_view()),
    path('teamMembers/<str:name>/', TeamMembers.as_view()),
    path('cliqueDetails/<str:name>/', CliqueDetails.as_view()),
    path('cliqueMembers/<str:name>/', CliqueMembers.as_view()),    
    path('invitationDetails/<str:code>/', InvitationDetails.as_view()),
    path('cliqueEvents/<str:name>/', CliqueEvents.as_view()),
    path('userSoloEvents/<str:username>/', UserSoloEvents.as_view()),
    path('userSchedules/<str:username>/', UserSchedules.as_view()),
    path('scheduleTimeFrames/<int:scheduleId>/', ScheduleTimeFrames.as_view()),
    path('cliqueAnnouncements/<str:name>/', CliqueAnnouncements.as_view())
]