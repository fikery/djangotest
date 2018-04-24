from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Post,Product,PProduct,PPhote
from django.template.loader import get_template
import random,datetime
from mainsite import models,forms
from django.template import RequestContext


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
    hour=now.timetuple().tm_hour
    tv=tv_list[int(tvno)]
    html=template.render(locals())
    return HttpResponse(html)

def carlist(request,maker='0'):
    car_maker=['宝马','福特','本田','马自达','尼桑','丰田']
    car_list=[
        [],['fiesta','福克斯','modeo','ecosport','kuga','mustang'],['fit','odyssey','cr-v','city','nsx'],
        ['马自达3','马自达5','马自达6','cx-3','cx-5','mx-5'],
        ['march','tida','march','livina','sentra','teana','x-trail','juke','murano'],
        ['凯美瑞','altis','yaris','86','prius','vios','rav4','wish']
    ]
    maker=int(maker)
    maker_name=car_maker[maker]
    cars=car_list[maker]
    template=get_template('carlist.html')
    html=template.render(locals())
    return HttpResponse(html)

def pindex(request):
    products=PProduct.objects.all()
    template=get_template('pindex.html')
    html=template.render(locals())
    return HttpResponse(html)

def phonedetail(request,id):
    try:
        product=PProduct.objects.get(id=id)
        images=PPhote.objects.filter(product=product)
    except:
        pass
    template=get_template('phonedetail.html')
    html=template.render(locals())
    return HttpResponse(html)

def mood(request):
    template=get_template('mood.html')
    posts=models.MPost.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods=models.Mood.objects.all()
    try:
        user_id=request.get['user_id']
        user_pass=request.get['user_pass']
        user_post=request.get['user_post']
        user_mood=request.get['mood']
    except:
        user_id=None
        message='请输入数据'
    if user_id:
        mood=models.Mood.objects.get(status=user_mood)
        post=models.MPost.objects.create(mood=mood, nickname=user_id,del_pass=user_pass,message=user_post)
        post.save()
        message='成功存储，将会在审核后显示'

    html=template.render(locals())
    return HttpResponse(html)

def flisting(request):
    template=get_template('flisting.html')
    posts=models.MPost.objects.filter(enabled=True).order_by('-pub_time')[:50]
    moods=models.Mood.objects.all()

    html=template.render(locals())

    return HttpResponse(html)

def fposting(request):
    template=get_template('fposting.html')
    moods=models.Mood.objects.all()
    message='发布信息请完整填写内容'

    # request_context=RequestContext(request)
    # request_context.push(locals())
    html=template.render(context=locals(),request=request)

    return HttpResponse(html)

def contact(request):
    form=forms.ContactForm()
    template=get_template('contact.html')
    html=template.render(context=locals(),request=request)
    return HttpResponse(html)