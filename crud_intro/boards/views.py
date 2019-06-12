from django.shortcuts import render, redirect
from .models import Board, Comment
from IPython import embed


# Create your views here.
def index(request):
    boards = Board.objects.all()
    context = {'boards': boards}
    return render(request, 'boards/index.html', context)


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title') # 글 제목
        content = request.POST.get('content') # 글 내용
        image = request.FILES.get('image') # 이미지
        board = Board(title=title, content=content, image=image)
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        return render(request, 'boards/create.html')


def detail(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    # 현재 게시글이 가지고 있는 모든 댓글
    # comments = board.comment_set.all()
    comments = board.comment_set.order_by('-pk')
    context = {
        'board': board,
        'comments': comments,
    }
    return render(request, 'boards/detail.html', context)


def delete(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == 'POST':
        board.delete()
        return redirect('boards:index')
    else:
        return redirect('boards:detail', board.pk)


def update(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method =='POST':
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.image = request.FILES.get('image')
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        context = {'board': board,}
        return render(request, 'boards/update.html', context)


def comments_create(request, board_pk):
    # 댓글을 달 게시물
    board = Board.objects.get(pk=board_pk)
    if request.method == 'POST':
        # form 에서 넘어온 댓글 정보
        content = request.POST.get('content')
        # 댓글 생성 및 저장
        comment = Comment(board=board, content=content)
        # comment = Comment(board_id=board.pk, content=content)
        comment.save()
        return redirect('boards:detail', board.pk)
        # return redirect('boards:detail', comment.board_id)
    else:
        return redirect('boards:detail', board.pk)


def comments_delete(request, board_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        comment.delete()
    return redirect('boards:detail', board_pk)



