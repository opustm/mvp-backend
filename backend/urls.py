from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from .views import documentation

urlpatterns = [
    path('', documentation, name='documentation'),
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('token-auth/', obtain_jwt_token),
]