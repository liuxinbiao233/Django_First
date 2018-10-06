from django.contrib import admin
from .models import ReadedNum,ReadDetail

@admin.register(ReadedNum)
class BlogNumAdmin(admin.ModelAdmin):
    list_display = ('readed_num','content_object')

@admin.register(ReadDetail)
class BlogNumAdmin(admin.ModelAdmin):
    list_display = ('date','readed_num','content_object')
