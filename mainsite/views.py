from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Post,Product
from django.template.loader import get_template
import random,datetime


# Create your views here.
def index(request):
    template=get_template('index.html')
    quotes = [
        '一二三四五，上山打老虎', '我去年买了个登山包', '你可别说了，算我球球你了'
    ]
    html = template.render({'quote': random.choice(quotes)})
    return HttpResponse(html)

def about(request):
    template=get_template('about.html')
    html=template.render()
    return HttpResponse(html)

def listing(request):
    template=get_template('list.html')
    products=Product.objects.all()

    html=template.render({'products':products})

    return HttpResponse(html)

def disp_detail(request,sku):
    try:
        p=Product.objects.get(sku=sku)
    except:
        raise Http404('找不到指定商品编号')
    template=get_template('disp.html')
    html=template.render({'product':p})

    return HttpResponse(html)

def post(request,year,month,day,post_num):
    html='<h2>{}/{}/{}:当前查看编号:{}'.format(year,month,day,post_num)
    return HttpResponse(html)

def video(request,tvno='0'):
    tv_list=[{'name':'CCTV 中文国际频道','tvcode':'vCDDYb_M2B4'},{'name':'台湾中天新闻频道','tvcode':'wUPPkSANpyo'},]
    template=get_template('video.html')
    now=datetime.datetime.now()
    # tvno=tvno
    tv=tv_list[int(tvno)]
    html=template.render(locals())
    return HttpResponse(html)