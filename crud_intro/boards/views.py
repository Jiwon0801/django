from django.shortcuts import render, redirect
from .models import Board
from IPython import embed


# Create your views here.
def index(request):
    boards = Board.objects.all()
    context = {'boards': boards}
    return render(request, 'boards/index.html', context)


# CREATE
## 글 작성 페이지
# def new(request):
#     return render(request, 'boards/create.html')


## DB에 연동
def create(request):
    # request 가 POST로 왔을때는 create
    if request.method == 'POST':
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
        return redirect('boards:detail', board.pk)

    # request method가 GET으로 왔을때는 new
    else:
        return render(request, 'boards/create.html')


    # create.html 페이지를 render
    # content = {
    #     'title': title,
    #     'content': content,
    # }



def detail(request, pk):
    #요청으로 들어온 pk 값으로 해당 글을 찾아옴
    board = Board.objects.get(pk=pk)
    context = {'board': board}
    return render(request, 'boards/detail.html', context)


def delete(request, pk):
    board = Board.objects.get(pk=pk)
    if request.method == 'POST':
        board.delete()
        # return redirect('/boards/')
        return redirect('boards:index')
    else:
        return redirect('boards:detail', board.pk)



# def edit(request, pk):
#     board = Board.objects.get(pk=pk)
#     context = {'board': board}
#     return render(request, 'boards/update.html', context)


def update(request, pk):
    #UPDATE
    board = Board.objects.get(pk=pk)
    if request.method == 'POST':
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect('boards:detail', board.pk)
    # EDIT
    else:
        context = {'board': board}
        return render(request, 'boards/update.html', context)

    # return redirect(f'/boards/{board.pk}/')

