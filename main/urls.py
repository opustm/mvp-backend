from django.urls import path, include
from .views import current_user, UserList, csrf, ping, index, team, UserDetail, TeamList, TeamDetail, EventList, EventDetail, InvitationList, InvitationDetail, TeamMembersByTeamId, TeamMembersByTeamName

urlpatterns = [
    path('', index),
    path('current_user/', current_user),
    path('user/<str:username>/', UserDetail.as_view()),
    path('team/<str:name>/', TeamDetail.as_view()),
    path('teamMembersByTeamid/<int:teamid>/', TeamMembersByTeamId.as_view()),#do we REALLY need this one?
    path('teamMembers/<str:name>/', TeamMembersByTeamName.as_view()),
    path('invitation/<str:code>/', InvitationDetail.as_view()),
    path('event/<int:pk>/', EventDetail.as_view()),
    # path('csrf/', csrf),
    # path('ping/', ping),
]