from django.contrib import admin
from .models import Post,Product,Maker,PProduct,PModel,PPhote
from mainsite import models
# Register your models here.
admin.site.register(Post)
admin.site.register(Product)
admin.site.register(Maker)
admin.site.register(PPhote)
admin.site.register(PModel)
# admin.site.register(PProduct)
class PProductAdmin(admin.ModelAdmin):
    list_display = ('pmodel','nickname','price','year')
    search_fields = ('nickname',)
    ordering = ('-price',)

admin.site.register(PProduct,PProductAdmin)

#窗体
class MPostAdmin(admin.ModelAdmin):
    list_display = ('nickname','message','enabled','pub_time')
    ordering = ('-pub_time',)
admin.site.register(models.Mood)
admin.site.register(models.MPost,MPostAdmin)

#session
admin.site.register(models.MyUser)

admin.site.register(models.Profile)

admin.site.register(models.Diary)