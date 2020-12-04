from django.urls import path, include
from .views import current_user, UserList, index, team, UserDetail, TeamList, TeamDetail, EventList, EventDetail, UserEventList, UserEventDetail, InvitationList, InvitationDetail, TeamMembersByTeamname, ScheduleTimeFrameList, ScheduleTimeFramesByUsername

urlpatterns = [
    path('', index),
    path('current_user/', current_user),
    path('user/<str:username>/', UserDetail.as_view()),
    path('team/<str:name>/', TeamDetail.as_view()),
    path('teamMembers/<str:name>/', TeamMembersByTeamname.as_view()),
    path('invitation/<str:code>/', InvitationDetail.as_view()),
    path('event/<int:pk>/', EventDetail.as_view()),
    path('userEvent/<int:pk>/', UserEventDetail.as_view()),
    path('scheduleTimeFramesByUsername/<str:username>/', ScheduleTimeFramesByUsername.as_view())

]