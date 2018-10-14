import datetime
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from .models import ReadedNum,ReadDetail


def read_recore_one_read(request,obj):
    ct = ContentType.objects.get_for_model(obj)
    key="%s_%s_read" %(ct.model,obj.pk)#用来使用cookies的

    if not request.COOKIES.get(key):
        #总阅读数+1
        readnum,created=ReadedNum.objects.get_or_create(content_type=ct,object_id=obj.pk)
        readnum.readed_num +=1
        readnum.save()

        #当天阅读数+1
        date=timezone.now().date()
        readDetail,created=ReadDetail.objects.get_or_create(content_type=ct,object_id=obj.pk,date=date)
        readDetail.readed_num+=1
        readDetail.save()
    return key



def get_seven_days_read_data(content_type):
    today=timezone.now().date()
    read_nums=[]
    dates=[]

    for i in range(7,0,-1):
        date=today-datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))
        read_details=ReadDetail.objects.filter(content_type=content_type,date=date)
        result=read_details.aggregate(read_num_sum=Sum('readed_num'))
        read_nums.append(result['read_num_sum'] or 0)
    return dates,read_nums

