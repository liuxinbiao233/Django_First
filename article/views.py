from django.shortcuts import render,render_to_response,get_object_or_404#后者是前者的简化版本
from django.http import HttpResponse,Http404
from .models import Article

# Create your views here.
'''
def article_detail(request,article_id):
	try:
		article=Article.objects.get(id=article_id)
		context = {}
		context['article_objects']=article#把传取到article（函数id）的对象，传给article_objects
		#return render(request,"article_detail.html",context)#render会产生response的响应的界面，第一个参数为request，第二个参数为模板地址，第三个返回变量
		return render_to_response("article_detail.html",context)
	except Article.DoesNotExist:
		raise Http404("not exist")
'''
def article_detail(request,article_id):
	article=get_object_or_404(Article,pk=article_id)#第一个是模型，第二个是条件(pk是条件的缩写)
	context = {}
	context['article_objects']=article
	return render_to_response("article_detail.html",context)
	
def article_list(request):
	articles = Article.objects.filter(is_deleted=False)#all()#获取全部对象#filter是为了筛选目的
	context={}
	context['articles']=articles
	return render_to_response("article_list.html",context)
