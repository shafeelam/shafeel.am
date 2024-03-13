from calendar import HTMLCalendar
from django.shortcuts import render
from django.http import HttpResponse
from .models import facts
from .models import progress
from django.contrib import messages
from .forms import enquiryForm

# Create your views here.

def index(request):
    fact = facts()
    fact.hapclients = 20
    fact.project = 30
    fact.hosupport = 1000
    fact.award = 1
    
    progress1 = progress()
    progress1.skill = "HTML"
    progress1.skillnow = 100
    
    progress2 = progress()
    progress2.skill = "CSS"
    progress2.skillnow = 90
    
    progress3 = progress()
    progress3.skill = "JAVASCRIPT"
    progress3.skillnow = 55
    
    progresses = [progress1,progress2,progress3]
    
    progress4 = progress()
    progress4.skill = "PYTHON"
    progress4.skillnow = 90
    
    progress5 = progress()
    progress5.skill = "DJANGO"
    progress5.skillnow = 95
    
    progress6 = progress()
    progress6.skill = "WordPress"
    progress6.skillnow = 95
    
    progresses1 = [progress4,progress5,progress6]
    
    return render(request, 'index.html', {'fact':fact,'progresses':progresses,'progresses1':progresses1})

def enquiry(request):
    responsed = {}
    if request.method =='POST':
        form = enquiryForm(request.POST)
        if form.is_valid():
            form.save()
            responsed['msged'] = 'you will get the reply from us as soon as possible'
            return render(request,'index.html',responsed)
    else:
        messages.info(request,'something went wrong') 
        return render(request,'index.html')
        
    
