from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
import os

class Post(models.Model):
    title = models.CharField(max_length=30) #제목
    content = MarkdownxField() #내용

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    create_at = models.DateTimeField(auto_now_add=True) #작성일
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) #작성자 정보, 작성자가 삭제될 떄, 포스트 작성자명 NULL로

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'  #해당 포스트의 pk 값, 해당 포스트의 title 값

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_content_markdown(self):
        return markdown(self.content)