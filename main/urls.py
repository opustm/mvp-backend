from django.urls import path, include
from .views import current_user, UserList, UserToDos, index, UserDetails, CliqueDetails, CliqueEvents, UserSoloEvents, InvitationDetails, CliqueMembers, UserSchedules, ScheduleTimeFrames, CliqueAnnouncements, CliqueCliqueMessages, UserDirectMessagesSent, UserDirectMessagesRecieved

urlpatterns = [
    path('', index),
    path('currentUser/', current_user),
    path('addUsers/', UserList.as_view()),
    path('userDetails/<str:username>/', UserDetails.as_view()),
    path('cliqueDetails/<str:name>/', CliqueDetails.as_view()),
    path('cliqueMembers/<str:name>/', CliqueMembers.as_view()),    
    path('invitationDetails/<str:inviteeEmail>/', InvitationDetails.as_view()),
    path('cliqueEvents/<str:name>/', CliqueEvents.as_view()),
    path('userSoloEvents/<str:username>/', UserSoloEvents.as_view()),
    path('userSchedules/<str:username>/', UserSchedules.as_view()),
    path('scheduleTimeFrames/<int:scheduleId>/', ScheduleTimeFrames.as_view()),
    path('cliqueMesssages/<str:name>/', CliqueCliqueMessages.as_view()),
    path('userDirectMessagesSent/<str:username>/', UserDirectMessagesSent.as_view()),
    path('userDirectMessagesRecieved/<str:username>/', UserDirectMessagesRecieved.as_view()),
    path('userToDos/<str:username>/', UserToDos.as_view())
]
