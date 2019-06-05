from django.shortcuts import render, redirect
from .models import Board


# Create your views here.
def index(request):
    boards = Board.objects.all()
    context = {'boards': boards}
    return render(request, 'boards/index.html', context)


# CREATE
## 글 작성 페이지
def new(request):
    return render(request, 'boards/new.html')


## DB에 연동
def create(request):
    # new에서 넘어오는 제목과 내용을 저장
    title = request.POST.get('title')
    content = request.POST.get('content')
    # orm - title과 content에 위에서 넘어온 값을 저장
    board = Board()
    board.title = title
    board.content = content
    # board = Board(title=title, content, content)

    # DB에 저장
    board.save()
    # create.html 페이지를 render
    content = {
        'title': title,
        'content': content,
    }
    return redirect(f'/boards/{board.pk}')

def detail(request, pk):
    #요청으로 들어온 pk 값으로 해당 글을 찾아옴
    board = Board.objects.get(pk=pk)
    context = {'board': board}
    return render(request, 'boards/detail.html', context)
