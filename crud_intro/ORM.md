# SQLite



### CRUD

- Create
- Read = Select
- Update
- Delete





### ORM(Object-Relational Mapping)

- Database : SQL statement <- ORM -> Python Object : Python Code

![ORM](https://cdn-images-1.medium.com/max/1600/0*UkOqM_a_agYwUOoV)





### ORM 사용

- __models.py 작성__ ( layout )

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

  - OMR이 자동으로 SQL과의 변환값을 만들어 줌 (__Python object 생성__)

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
```

