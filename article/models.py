from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=30)
	content = models.TextField()
	created_time=models.DateTimeField(auto_now_add=True)#自动生成日期
	last_update_time=models.DateTimeField(auto_now=True)#自动生成变更的最后日期
	author=models.ForeignKey(User,on_delete=models.DO_NOTHING,default=1)
	is_deleted=models.BooleanField(default=False)
	readed_num=models.IntegerField(default=0)
	def __str__(self):#设置模型 定制admin
		return "<Article:%s>" % self.title
