from django.urls import path, include
from .views import current_user, UserList, index, team, UserDetail, TeamList, TeamDetail, EventList, EventDetail, InvitationList, InvitationDetail, TeamMembersByTeamname, WeekScheduleDetail, WeekScheduleList, WeekSchedulesByUsername

urlpatterns = [
    path('', index),
    path('current_user/', current_user),
    path('user/<str:username>/', UserDetail.as_view()),
    path('team/<str:name>/', TeamDetail.as_view()),
    path('teamMembers/<str:name>/', TeamMembersByTeamname.as_view()),
    path('invitation/<str:code>/', InvitationDetail.as_view()),
    path('event/<int:pk>/', EventDetail.as_view()),
    path('schedule/<int:pk>/', WeekScheduleDetail.as_view()),
    path('weekSchedulesByUsername/<str:username>/', WeekSchedulesByUsername.as_view())
]