from django.shortcuts import render
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required



def form_view (request):
    # return render(request,'form.html')
    if request.method == 'POST':
        form = AuthentificationForm(request.POST)
        if form.is_valid():
            return render(request,"vhod.html")
    else:
        form = AuthentificationForm()
    return render(request,"registr.html",{'form':form})

def vhod (request):
    return render(request,"vhod.html")

def page (request):
    return render(request,"first_page.html")

