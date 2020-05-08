from django.urls import path

from . import views

app_name = 'bridge'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:bridge_id>/', views.detail, name='detail'),
    path('add_county/', views.add_county, name='add_county'),
]