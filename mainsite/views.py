from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
from .models import Post,Product,PProduct,PPhote
from django.template.loader import get_template
import random,datetime,time
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
    if request.method=='POST':
        form=forms.ContactForm(request.POST)
        if form.is_valid():
            message='感谢来信'
            user_name=form.cleaned_data['user_name']
            user_city=form.cleaned_data['user_city']
            user_school=form.cleaned_data['user_school']
            user_email=form.cleaned_data['user_email']
            user_message=form.cleaned_data['user_message']

            mail_body='''
            姓名:{}
            城市:{}
            学生:{}
            建议:{}
            '''.format(user_name,user_city,user_school,user_message)
            email=EmailMessage('来自【不吐不快】网站的网友意见',mail_body,user_email,['liuyongbin0011@gmail.com'])
            email.send()
        else:
            message='请检查输入是否正确'
    else:
        form=forms.ContactForm()
    template=get_template('contact.html')
    html=template.render(context=locals(),request=request)
    return HttpResponse(html)

#session
def login(request):
    if request.method=='POST':
        login_form=forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name=request.POST['username'].strip()
            login_password=request.POST['password']
            # try:
                # user=models.User.objects.get(name=login_name)#使用自定义的User类
                # if user.password==login_password:
                #     request.session['username']=user.name
                #     request.session['useremail']=user.email
                #     messages.add_message(request,messages.SUCCESS,'成功登录')
                #     return redirect('/user/')
                # else:
                #     messages.add_message(request,messages.WARNING,'密码错误，请重试')
            # except:
            #     messages.add_message(request,messages.WARNING,'用户名错误，请重试')
            user = authenticate(username=login_name, password=login_password)  # 系统User,验证登录
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    messages.add_message(request, messages.SUCCESS, '成功登录')
                    return redirect('/user/')
                else:
                    messages.add_message(request, messages.WARNING, '账号未启用')
            else:
                messages.add_message(request, messages.WARNING, '登录失败')
        else:
            messages.add_message(request,messages.INFO,'请检查输入内容')
    else:
        login_form=forms.LoginForm()

    template=get_template('userlogin.html')
    html=template.render(context=locals(),request=request)
    return HttpResponse(html)

def login_index(request,pid=None,del_pass=None):
    # 采用自定义user类
    # if 'username' in request.session:
    #     username=request.session['username']
    #     useremail=request.session['useremail']
    #采用系统user类
    if request.user.is_authenticated:
        username=request.user.username
        useremail=request.user.email
        try:
            user=User.objects.get(username=username)
            diaries=models.Diary.objects.filter(user=user).order_by('-ddate')
        except:
            pass
    messages.get_messages(request)
    template=get_template('userindex.html')
    html=template.render(context=locals(),request=request)
    return HttpResponse(html)

# @login_required(login_url='/login/')
# def userinfo(request):
#     # if 'username' in request.session:
#     #     username=request.session['username']
#     # else:
#     #     return redirect('/login/')
#     # try:
#     #     userinfo=models.User.objects.get(name=username)
#     # except:
#     #     pass
#     if request.user.is_authenticated:
#         username=request.user.username
#         try:
#             user=User.objects.get(username=username)
#             userinfo=models.Profile.objects.get(user=user)
#         except:
#             pass
#     template=get_template('userinfo.html')
#     html=template.render(context=locals(),request=request)
#     return HttpResponse(html)

def logout(request):
    auth.logout(request)
    messages.add_message(request,messages.INFO,'注销成功')
    return redirect('/login/')

@login_required(login_url='/login/')
def userPosting(request):
    if request.user.is_authenticated:
        username=request.user.username
        useremail=request.user.email
    messages.get_messages(request)

    if request.method=='POST':
        user=User.objects.get(username=username)
        diary=models.Diary(user=user)
        post_form=forms.DiaryForm(request.POST,instance=diary)
        if post_form.is_valid():
            messages.add_message(request,messages.INFO,'保存成功')
            post_form.save()
            return redirect('/user/')
        else:
            messages.add_message(request,messages.INFO,'请检查字段是否填写完整')
    else:
        post_form=forms.DiaryForm()
        messages.add_message(request,messages.INFO,'如果要发布日记，请填写完整字段')

    template=get_template('userposting.html')
    html=template.render(context=locals(),request=request)
    return HttpResponse(html)

#注册
@login_required(login_url='/login/')
def userinfo(request):
    if request.user.is_authenticated:
        username=request.user.username
    user=User.objects.get(username=username)
    try:
        profile=models.Profile.objects.get(user=user)
    except:
        profile=models.Profile(user=user)
    if request.method=='POST':
        profile_form=forms.ProfileForm(request.POST,instance=profile)
        if profile_form.is_valid():
            messages.add_message(request, messages.INFO, '保存成功')
            profile_form.save()
            return redirect('/userinfo')
        else:
            messages.add_message(request, messages.INFO, '请检查字段是否填写完整')
    else:
        profile_form=forms.ProfileForm()

    template=get_template('userinfo.html')
    html=template.render(context=locals(),request=request)
    return HttpResponse(html)
