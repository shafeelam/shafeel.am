
from django.contrib import messages
from genericpath import exists
from django.shortcuts import render , redirect
from django.contrib.auth.models import auth,User
from .forms import messageForm

# Create your views here.

def register(request):
    responsedik = {}
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
          if len(password1) > 8 :
            if User.objects.filter(username=username).exists():
              messages.info(request,'Username already exists..')
              return redirect('register')
            elif User.objects.filter(email=email).exists():
              messages.info(request,'Email already exists..')
              return redirect('register')
            else:
              user = User.objects.create_user(username=username , password=password1, email=email , last_name=last_name , first_name=first_name)
              user.save()
              responsedik['msg'] = 'user added successfully..'
              return render(request,'register.html',responsedik)
          else:
             messages.info(request,'Password must contain 8 letters') 
             return redirect('register')
        else:
          messages.info(request,'Password not matching... Try again')
          return redirect('register')
    else:
      return render(request,'register.html')
    
    
def login(request):
  responsedi = {}
  if request.method == 'POST':
    username = request.POST['username']
    password =  request.POST['password']
    
    user = auth.authenticate(username=username , password=password)
    if user is not None:
      auth.login(request,user)
      return render(request,"user.html")
    
    else:
       responsedi['msge']='Username and password doesnot match'
       return render(request,'login.html',responsedi)
    
  else:
    return render(request,'login.html')
  
def messages(request):
    responsemsg = {}
    if request.method =='POST':
        form = messageForm(request.POST)
        if form.is_valid():
            form.save()
            responsemsg['msged'] = 'you will get the reply from us as soon as possible'
            return render(request,'user.html',responsemsg)
    else:
        messages.info(request,'something went wrong') 
        return render(request,'user.html')



def logout(request):
  auth.logout(request)
  return redirect('/')
  