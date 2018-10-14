from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


# Create your models here.
class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="comments",on_delete=models.CASCADE)#反向解析，找到所有的评论

    root=models.ForeignKey('self',related_name="root_comments",null=True,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',related_name="parent_comments",null=True,on_delete=models.CASCADE)
    reply_to=models.ForeignKey(User,related_name="replies",null=True,on_delete=models.CASCADE)#反向解析，找到所相关的回复


    def __str__(self):
        return self.text


    class Meta:
        ordering = ['comment_time']

