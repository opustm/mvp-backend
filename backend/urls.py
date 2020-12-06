from django.contrib import admin
from django.urls import path, include
from .views import documentation
from .router import router
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.authtoken import obtain_auth_token



urlpatterns = [
    path('token-auth/', obtain_jwt_token),
    path('', documentation, name='documentation'),
    path('main/', include('main.urls')),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]