from django import forms
from django.forms import ModelForm  #for class PushForm
from app.models import PushModel  #for class PushForm

class PushFormAlias(forms.Form):
    msg = forms.CharField(max_length=100,label='推送消息')
    url = forms.URLField(label='网址')

class PushForm(forms.ModelForm):
    class Meta:
        model = PushModel
        fields = '__all__'
