from django.urls import path, include
from .views import current_user, UserList, csrf, ping, index

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('csrf/', csrf),
    path('ping/', ping),
    path('', index, name='index'),
]