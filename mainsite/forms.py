from django import forms
from django.forms import ModelForm
from . import models


class ContactForm(forms.Form):
    CITY = [
        ['TP', '台北'], ['BJ', '北京'], ['SHH', '上海'], ['NA', '其他']
    ]
    user_name = forms.CharField(label='姓名', max_length=50, initial='王大锤')
    user_city = forms.ChoiceField(label='城市', choices=CITY)
    user_school = forms.BooleanField(label='毕业', required=True)
    user_email = forms.EmailField(label='邮件')
    user_message = forms.CharField(label='建议', widget=forms.Textarea)

class LoginForm(forms.Form):
    username=forms.CharField(label='用户名',max_length=10)
    password=forms.CharField(label='密码',widget=forms.PasswordInput())


class DateInput(forms.DateInput):
    input_type = 'date'

class DiaryForm(ModelForm):

    class Meta():
        model=models.Diary
        fields=['budget','weight','note','ddate']
        widgets={
            'ddate':DateInput(),
        }

    def __init__(self,*args,**kwargs):
        super(DiaryForm,self).__init__(*args,**kwargs)
        self.fields['budget'].label='花费(元)'
        self.fields['weight'].label='体重(kg)'
        self.fields['note'].label='笔记'
        self.fields['ddate'].label='日期'

#注册
class ProfileForm(forms.ModelForm):
    class Meta():
        model=models.Profile
        fields=['height','male','website']

    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)
        self.fields['height'].label='身高(cm)'
        self.fields['male'].label='是否男性'
        self.fields['website'].label='网站'