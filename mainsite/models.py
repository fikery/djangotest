from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title=models.CharField('标题',max_length=200)
    slug=models.CharField('地址',max_length=200)
    body=models.TextField('内容')
    pub_date=models.DateTimeField('发布时间',default=timezone.now)

    class Meta:
        ordering=('-pub_date',)

    def __str__(self):
        return self.title

class Product(models.Model):
    sizes=(
        ('S','small'),
        ('M','medium'),
        ('L','large'),
    )
    sku=models.CharField('编号',max_length=5)
    name=models.CharField('名称',max_length=20)
    price=models.PositiveIntegerField('价格')
    size=models.CharField('尺寸',max_length=1,choices=sizes)
    qty=models.PositiveIntegerField('库存',default=0)

    def __str__(self):
        return self.name


class Maker(models.Model):
    name=models.CharField('制造商',max_length=10)
    country=models.CharField('国家',max_length=10)
    def __str__(self):
        return self.name

class PModel(models.Model):
    maker=models.ForeignKey(Maker,on_delete=models.CASCADE)
    name=models.CharField('名称',max_length=20)
    url=models.URLField(default='https://sale.vmall.com/p20.html')
    def __str__(self):
        return self.name

class PProduct(models.Model):
    pmodel=models.ForeignKey(PModel,on_delete=models.CASCADE,verbose_name='型号')
    nickname=models.CharField('简称',max_length=20,default='华为p20')
    description=models.TextField(verbose_name='描述',default='暂无')
    year=models.PositiveIntegerField(verbose_name='出厂年份',default=2018)
    price=models.PositiveIntegerField(verbose_name='价格',default=0)
    def __str__(self):
        return self.nickname

class PPhote(models.Model):
    product=models.ForeignKey(PProduct,on_delete=models.CASCADE)
    description=models.CharField(max_length=20,default='产品照片')
    url=models.URLField(default='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1524129042512&di=176d16313df19f220cffff91e3bcacb2&imgtype=0&src=http%3A%2F%2Fimg1.mydrivers.com%2Fimg%2F20180327%2F9d40cf99ba02469fbecd444b67c1761a.jpg')
    def __str__(self):
        return self.description

class Mood(models.Model):
    status=models.CharField('状态',max_length=10,null=False)
    def __str__(self):
        return self.status
class MPost(models.Model):
    mood=models.ForeignKey('Mood',on_delete=models.CASCADE)
    nickname=models.CharField('昵称',max_length=10,default='佚名')
    message=models.TextField('内容',null=False)
    del_pass=models.CharField(max_length=10)
    pub_time=models.DateTimeField(auto_now=True)
    enabled=models.BooleanField(default=False)
    def __str__(self):
        return self.message

#活用session
class MyUser(models.Model):
    name=models.CharField(max_length=20,null=False)
    email=models.EmailField()
    password=models.CharField(max_length=20,null=False)
    enabled=models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    height=models.PositiveIntegerField(default=170)
    male=models.BooleanField(default=False)
    website=models.URLField(null=True)
    def __str__(self):
        return self.user.username

class Diary(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    budget=models.FloatField(default=0)
    weight=models.FloatField(default=0)
    note=models.TextField()
    ddate=models.DateField()
    def __str__(self):
        return '{}({})'.format(self.ddate,self.user)