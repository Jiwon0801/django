from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dinner/', views.dinner),
    path('hello/<name>/', views.hello),
    path('introduce/<name>/<int:age>/', views.introduce),
    path('times/<int:a>/<int:b>/', views.times),
    path('area/<int:r>/', views.area),
    path('dtl_example/', views.dtl_example),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('artii/', views.artii),
    path('result/', views.result),
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),
    path('static_example/', views.static_example),
]
