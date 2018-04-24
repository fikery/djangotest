from django import forms


class ContactForm(forms.Form):
    CITY = [
        ['TP', '台北'], ['BJ', '北京'], ['SHH', '上海'], ['NA', '其他']
    ]
    user_name = forms.CharField(label='姓名', max_length=50, initial='王大锤')
    user_city = forms.ChoiceField(label='城市', choices=CITY)
    user_school = forms.BooleanField(label='毕业', required=True)
    user_email = forms.EmailField(label='邮件')
    user_message = forms.CharField(label='建议', widget=forms.Textarea)
