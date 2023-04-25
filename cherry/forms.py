from django import forms



def check_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('data is not valid')


class StudentForm(forms.Form):
    Name=forms.CharField(max_length=100,validators=[check_for_a])
    Age=forms.IntegerField()
    Email=forms.EmailField(max_length=100)
