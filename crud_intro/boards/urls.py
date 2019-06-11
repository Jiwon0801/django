from django.urls import path
from . import views

app_name = 'boards'
urlpatterns = [
    path('<int:board_pk>/update/', views.update, name='update'),  #GET(new), POST(create)
    # path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:board_pk>/delete/', views.delete, name='delete'),
    path('<int:board_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'), #GET(new), POST(create)
    # path('new/', views.new, name='new'), #get
    path('', views.index, name='index'),
    path('<int:board_pk>/comments/', views.comments_create, name='comments_create'), #POST
    path('<int:board_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete')
]
