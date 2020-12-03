from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from .views import documentation
from .router import router

urlpatterns = [
    path('', documentation, name='documentation'),
    path('', include('main.urls')),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('token-auth/', obtain_jwt_token)
]