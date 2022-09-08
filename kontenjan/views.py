from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse


from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def kontenjan(request):


    return render(request,"kontenjan.html")

def ebe21(request):
    items = Ebe.objects.all()
    context = {
        'items': items,
        'header':'Ebelik Bölümü 2021',

    }

    return render(request,"kontenjan.html",context)

def hemsire21(request):
    items = Hemsire.objects.all()
    context = {
        'items': items,
        'header':'Hemsire Bölümü 2021',

    }

    return render(request,"kontenjan.html",context)