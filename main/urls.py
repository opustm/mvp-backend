from django.urls import path, include
from .views import current_user, UserList, csrf, ping, index, team

urlpatterns = [
    path('', index),
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    # path('csrf/', csrf),
    # path('ping/', ping),
    path('team', team)
]