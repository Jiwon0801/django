## URL NAME

- __urls.py__

```python
from django.urls import path
from . import views

app_name = 'boards'
urlpatterns = [
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('new/', views.new, name='new'),
    path('', views.index, name='index')
]

```

- __html__

```html
    <a href="{% url 'boards:edit' board.pk %}">[수정]</a> <br>
    <a href="{% url 'boards:delete' board.pk %}">[삭제]</a> 
    <a href="{% url 'boards:index' %}">메인페이지로</a>
```



- __redirect__

```python
return redirect('boards:detail', board.pk)
```



## RESTful