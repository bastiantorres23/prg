from django.shortcuts import render, redirect
from .models import Zapato
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .form import *

def login(request):
    return render(request,"registration/login.html")


def Public(request):
    news=Zapato.objects.all()
    paginator = Paginator(news,3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"core/about.html",{'news':page_obj})


@login_required
def Inicio(request):
    return render(request,"core/home.html")



@login_required
def men(request):
    news=Zapato.objects.all()
    paginator = Paginator(news,3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"core/men.html",{'news':page_obj})


@login_required
def women(request):
    news=Zapato.objects.all()
    paginator = Paginator(news,3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"core/women.html",{'news':page_obj})



@login_required
def publicar(request):
    return render(request,"core/about.html")




def crear(request):
    if request.method == 'POST':
        maq_form = articleform(request.POST, request.FILES)
        if maq_form.is_valid():
            maq_form.save()
            return redirect('about.html')
    else:
        maq_form= articleform()
    return render(request,"fu/categoria.html",{'maq_form':maq_form})


def editar(request,n):
    maqui= Zapato.objects.get(Id = n)
    if request.method == 'GET':
        maq_form = articleform(instance= maqui)
    else:
        maq_form = articleform(request.POST, instance= maqui)
        if maq_form.is_valid():
            maq_form.save()
        redirect('about.html')
    return render(request,"fu/categoria.html",{'maq_form':maq_form})

def borr(request,n):
    bo= Zapato.objects.get(Id = n)
    bo.delete()
    return redirect('/about.html')





def exit(request):
    logout(request)
    return redirect('/')