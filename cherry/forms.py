from django import forms
from django.core import validators


def check_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('data is not valid')
    


def check_for_len(value):
    if len(value)<7:
        raise forms.ValidationError('length is not perfect')
    

class StudentForm(forms.Form):
    Name=forms.CharField(max_length=100,validators=[check_for_a,validators.MaxLengthValidator(5)])
    Age=forms.IntegerField()
    Email=forms.EmailField(max_length=100)
    Re_Enter_Email=forms.EmailField(max_length=100)
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)
    mobileno=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])

    def clean(self):
        e=self.cleaned_data['Email']
        r=self.cleaned_data['Re_Enter_Email']
        if e!=r:
            raise forms.ValidationError('Not Matched')
    
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('bot')