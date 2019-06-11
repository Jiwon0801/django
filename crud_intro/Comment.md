# Comment



### OneToOneField(1:1)

### ForeignKey(1:N)

### ManyToManyFields(N:N)





- python shell

```python
comment = Comment()
comment.content = 'first comment'
comment.board_id = board.pk
comment.save()

comment = Comment()
comment.content = 'second comment'
#외래키 설정, board에 바로 넣어도 pk 설정 가능
comment.board = board 
comment.save()

#외래키 설정
comment = Comment(board=board, content = 'third comment')

comment.save()


board.comment_set.all() #comment가 달려있는 board 쿼리 셋 출력
comments = board.comment_set.all()
comments.first().content

```



- __1에서 N을 참조할 때 : comment_set__
- __N에서 1을 참조할 때 :  .board__



```python
def detail(request, board_pk):
    #요청으로 들어온 pk 값으로 해당 글을 찾아옴
    board = Board.objects.get(pk=board_pk)
    #현재 게시글이 가지고 있는 모든 댓글
    # comments = board.comment_set.all()
    comments = board.comment_set.order_by('-pk') # 역순
    context = {'board': board, 'comments': comments}
    return render(request, 'boards/detail.html', context)
```



```html
<!--detail.html-->

<!--댓글 리스트로 출력-->
    {% for comment in comments %}
        <li>{{ comment.content }} </li>
    {% endfor %}
```

