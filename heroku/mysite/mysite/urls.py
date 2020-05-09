from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('bridge/', include('bridge.urls')),
    path('admin/', admin.site.urls),
]
