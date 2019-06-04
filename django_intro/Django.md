#  Django



### MTV  패턴

- M: Model ( 데이터 관리)  __부가적인 메타데이터를 가진 db의 구조__
- T:  Template (사용자가 보는 화면)
- V: View (중간 관리자 - controller)
- HTTP Request  > urls.py(app 설정) >  Views  >  Template  >  client



![DJango_Structure](https://mdn.mozillademos.org/files/13931/basic-django.png)



### django 설치

```
pip install django

django-admin startproject 폴더이름 .

python manage.py runserver


## .settings.py
LANGUAGE_CODE = 'ko-kr'

# template, form 등에서  출력되는 시간
TIME_ZONE = 'Asia/Seoul'

# model에서도 사용자가 지정한 TIME_ZONE 값을 적용시키기 위해 False
USE_TZ = False


## .gitignore
https://www.gitignore.io/
django, pycharm


```



### application

- 하나의 프로젝트는 여러개의 어플리케이션 소유 가능

- ```
  python manage.py startapp 어플리케이션명(복수형)
  ```

- models.py : database

- __views.py__ : 함수 정의 부분

- app 등록:  __settings.py__

  - ```python
    # 폴더이름\settings.py
    INSTALLED_APPS = [
       #local apps
        'books.apps.BooksConfig',
        'pages.apps.PagesConfig',
        #third party apps
        #django apps
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    ```



### Coding 순서

1.  __views.py__
2.  __urls.py__
3.  __templates.py__





### DTL : django 내장 변수



### GET, POST

- Get : DB에서 데이터를 꺼내는 것 ->  DB 변화 x
- Post: DB에서 데이터 조작 -> DB 변화 o



### static 파일

- css, image, js와 같이 별도의 처리없이 파일 내용을 그대로 보여줘도 되는 파일들
- django는 오로지 app_name/static/ 만 바라 볼 수 있다.