from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/delete/', views.delete, name='delete'),
    path('<int:movie_pk>/scores/', views.scores_create, name='scores_create'),
    path('<int:movie_pk>/scores/<int:score_pk>/delete/', views.scores_delete, name='scores_delete'),
    path('<int:movie_pk>/update/', views.update, name='update'),

]
