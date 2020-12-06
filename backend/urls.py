from django.contrib import admin
from django.urls import path, include
from .views import documentation
from .router import router
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.authtoken import obtain_auth_token



urlpatterns = [
    path('', documentation, name='documentation'),
    path('', include('main.urls')),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('token-auth/', obtain_auth_token)
]