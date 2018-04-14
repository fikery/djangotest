from django.db import models
from django.utils import timezone
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