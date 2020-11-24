from django.urls import path, include
from .views import current_user, UserList, csrf, ping, index, team, UserDetail

urlpatterns = [
    path('', index),
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view())
    # path('team/', team),
    # path('csrf/', csrf),
    # path('ping/', ping),
]