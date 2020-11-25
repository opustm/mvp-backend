from django.urls import path, include
from .views import current_user, UserList, csrf, ping, index, team, UserDetail, TeamList, TeamDetail, EventList, InvitationList

urlpatterns = [
    path('', index),
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('teams/', TeamList.as_view()),
    path('teams/<int:pk>/', TeamDetail.as_view()),
    path('events/', EventList.as_view()),
    path('invitations/', InvitationList.as_view())
    # path('csrf/', csrf),
    # path('ping/', ping),
]