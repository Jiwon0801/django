# SQLite



### CRUD

- Create
- Read = Select
- Update
- Delete





### ORM(Object-Relational Mapping)

- __Database <-----> ORM <-----> Python Class__

![ORM](https://cdn-images-1.medium.com/max/1600/0*UkOqM_a_agYwUOoV)





### ORM 사용

- __models.py 작성__ ( layout, Python Class )

```python
# models.py
class Board(models.Model):
    # id (pk)는 기본적으로 처음 데이터 생성시 자동 생성
    # id =  models.AutoField(primary key = True)
    title = models.CharField(max_length=10)# string 길이 제한
    content = models.TextField()
    # auto_now_add : 생성일자 / db가 최초 저장시에만 적용
    # auto_now : 수정일자 / db가 새로 저장될 때마다 갱신
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```



- __makemigrations__ : migration 만들기 (설계도)

  - ORM이 자동으로 SQL과의 변환값을 만들어 줌 (__Python object 생성__)

  ```
  python manage.py makemigrations
  
  > 0001_initial.py
  > 0002_board_updated_at.py
  ```

  
    - SQL문 확인 (__SQL Statement__)
  
  ```
     python manage.py sqlmigrate app이름 migrations생성숫자
   ex) python manage.py sqlmigrate boards 0002
  ```




- __migrate__ : DB 생성 ( 테이블 생성)

  ```
    python manage.py migrate
   
  ```
  
  ```
  migrate -> db.sqlite3
  ```
  
  



### SQLite 설치

```
PATH : ;C:\sqlite

winpty sqlite3

code ~/.bash_profile
> alias sqlite3="winpty sqlite 3"

source ~/.bash_profile
```





### SQLite 사용

```
sqlite3 db.sqlite3

.tables

.schema 테이블 명

python manage.py sqlmigrate boards 0001
```





### CREATE, READ

```sql
# python manage.py shell
from boards.models import Board
```




```sqlite
Board.objects.all() = SELECT * FROM boards_board
```



- __인스턴스 객체 board로 인스턴스 변수(title)에 값('first')을 할당__


```sqlite
board = Board()
board.title = 'first'
board.content = 'djnago!'

board = Board(title='second', content='djngo!!')

board.save() #DB에 값 쓰기
board # 값 확인

```

- __.save()__

  - board  객체에 id가 없을 때는 create(추가)하고, 있으면 수정(update)

- __전체 조회__

  ```sqlite
  Board.objects.all() # 객체 확인
  ```

  

- __.create()__ = .save 포함

  ```sqlite
  Board.objects.create(title='third', content='djngo!!!')
  > return 값: <Board: Board object (3)>
  
  ```



- __WHERE__


```sqlite
SELECT * FROM boards_board WHERE title='hello'
 # .filter() : 여러개 뽑는게 default
boards = Board.objects.filter(title='hello')


SELECT * FROM boards_board WHERE title='hello' LIMIT 1;
boards = Board.objects.filter(title='hello').first()
```



- __특정 값 지정__

```sqlite
SELECT * FROM boards_board WHERE id=1 LIMIT 1;

board = Board.objects.get(id=1)
board = Board.objects.get(pk=1)

```




- __LIKE__

```sqlite
SELECT * FROM boards_board LIKE

boards = Board.objects.filter(content__contains = 'f1')
boards = Board.objects.filter(content__endswith = '!')

```




- __ORDER BY__

```sqlite
SELECT * FROM boards_board ORDER BY DESC

board = Board.objects.order_by('title')
boards = Board.objects.order_by('-title')

```




- __slicing__

```sqlite
 boards[1]
 boards[1:3]
```



- __UPDATE__

```sqlite
 board.title
>>'first'
<Board: 1글 - first: django!>

board.title = 'byebye'
board.save()
<Board: 1글 - byebye: django!>


```


- __DELETE__

```sqlite
board.delete()
```





###  POST를 쓰는 이유

- html 파일 줘(get)이 아닌 한 레코드(글)을 생성해줘
- 데이터 관련 정보는 url에 노출되면 안된다.
- DB를 건드리기 때문에 최소한의 신원확인이 필요하다. 즉 CSRF TOKEN을 통해 검증된 요청을 받아야 한다.

```html
# new.py

{% block content%}   
    <form action="/boards/create" methos="POST">
        {% csrf_token %}
        <label for="title">Title: </label>
    </form>
{% endblock%}
```



- __POST 요청은 HTML 문서를 랜더링 하지 않음__
- __요청을 처리하고 나서 결과를 보여주는게 아닌, 결과를 보기위한 페이지로 넘겨줌(redirect)__

```python
from django.shortcuts import render, redirect

title = request.POST.get('title')
content = request.POST.get('content')

return redirect('/boards/') #데이터를 보여주는 페이지 (to)
```

- create.html 필요 없음




###  사용자 관리
~~~
python manage.py createsuperuser

http://127.0.0.1:8000/admin/
~~~

```python
from .models import Board

# Register your models here.
admin.site.register(Board)
```





#### UPDATE, DELETE

- __특정한 하나의 값에 대해 동작__


```sqlite
board = Board()
board.title = 'first'
board.content = 'djnago!'

board = Board(title='second', content='djngo!!')

board.save() #DB에 값 쓰기
board # 값 확인
```