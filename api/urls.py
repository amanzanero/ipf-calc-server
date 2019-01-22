from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/', include('powerlifters.urls')),
    path('admin/', admin.site.urls),

    # for rest_framework
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
