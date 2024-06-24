from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate
def home(request):
    return render(request,'index.html')
def second(request):
    return render(request,'secondpage.html')
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})
    return redirect('login')
