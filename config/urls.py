from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
    path('api/auth/', include('rest_framework.urls')),  # Login/logout
    path('api/auth/', include('djoser.urls')),  # Endpoints de usuários
    path('api/auth/', include('djoser.urls.jwt')),  # Endpoints de JWT
]
