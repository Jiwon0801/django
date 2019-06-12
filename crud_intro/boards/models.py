from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail


# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = ProcessedImageField(
        upload_to='boards/images', # 저장 위치 (media 이후의 경로)
        processors=[Thumbnail(200,300)], # 처리할 작업 목록
        format='JPEG', # 저장 포맷
        options={'quality': 90}, # 추가 옵션들.
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}글 - {self.title}: {self.content}'


class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return self.content
        return f'<Board({self.board_id}): Comment({self.pk}-{self.content}>'









