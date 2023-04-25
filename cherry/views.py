from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from cherry.forms import *
def student(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            return HttpResponse(str(SFDO.cleaned_data))
        else:
            return HttpResponse('data is not valid')


    return render(request,'student.html',d)


