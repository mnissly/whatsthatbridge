from django.urls import path

from . import views

app_name = 'bridge'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('add_county/', views.add_county, name='add_county'),
]