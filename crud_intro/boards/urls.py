from django.urls import path
from . import views

app_name = 'boards'
urlpatterns = [
    path('<int:pk>/update/', views.update, name='update'),  #GET(new), POST(create)
    # path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'), #GET(new), POST(create)
    # path('new/', views.new, name='new'), #get
    path('', views.index, name='index')
]
