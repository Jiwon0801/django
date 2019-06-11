from django.shortcuts import render, redirect
from .models import Board, Comment
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


def detail(request, board_pk):
    #요청으로 들어온 pk 값으로 해당 글을 찾아옴
    board = Board.objects.get(pk=board_pk)
    #현재 게시글이 가지고 있는 모든 댓글
    # comments = board.comment_set.all()
    comments = board.comment_set.order_by('-pk')
    context = {'board': board, 'comments': comments}
    return render(request, 'boards/detail.html', context)


def delete(request, board_pk):
    board = Board.objects.get(pk=board_pk)
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


def update(request, board_pk):
    #UPDATE
    board = Board.objects.get(pk=board_pk)
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


def comments_create(request, board_pk):
    # 댓글 달 게시물
    board = Board.objects.get(pk=board_pk)
    if request.method == "POST":
        # submit에서 넘어온 댓글 정보
        content = request.POST.get('content')
        # 댓글 생성 및 저장
        comment = Comment(board=board, content=content)
        comment.save()
        return redirect('boards:detail', board.pk)
    else:
        return redirect('boards:detail', board.pk)


def comments_delete(request, board_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == "POST":
        comment.delete()
    return redirect('boards:detail', board_pk)
    # else:
    #     return redirect('boards:detail', board_pk)
