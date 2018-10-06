from django.db import models
from django.db.models.fields import exceptions
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from read_record.models import ReadedNum
from read_record.models import ReadNumExpandMethod

class BlogType(models.Model):
    type_name=models.CharField(max_length=15)

    def __str__(self):
        return self.type_name


class Blog(models.Model,ReadNumExpandMethod):
    blog_type=models.ForeignKey(BlogType,on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=50)
    content=RichTextUploadingField()
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    created_time=models.DateTimeField(auto_now_add=True)
    readed_num=models.IntegerField(default=0)
    last_updated_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<Blog:%s>" % self.title

    def Meta(self):
        ordering = ['-created_time']

