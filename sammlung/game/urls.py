from django.urls import path, include
from . import views

app_name = 'game'
urlpatterns = [
    path('', views.game_view,  name='game'),
    path('detail/<str:pk>/', views.detail_view,  name='detail'),
    path('update/<str:pk>/', views.update_view,  name='update'),
    path('create/', views.create_view,  name='create'),
    path('delete/<str:pk>/', views.delete_view,  name='delete'),
]