from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30) #제목
    content = models.TextField() #내용

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    create_at = models.DateTimeField(auto_now_add=True) #작성일
    #author #작성자 정보

    def __str__(self):
        return f'[{self.pk}]{self.title}' #해당 포스트의 pk 값, 해당 포스트의 title 값

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'