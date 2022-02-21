from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blood_Bank, Districts, Centers


# Create your views here.
def index(request):
    obj = Blood_Bank.objects.all()
    return render(request, "index.html", {'result': obj})


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def wayanad(request):
    return render(request, "wayanad.html")


def thrissur(request):
    return render(request, "thrissur.html")


def alappuzha(request):
    return render(request, "alappuzha.html")


def ernakulam(request):
    return render(request, "ernakulam.html")


def idukki(request):
    return render(request, "idukki.html")


def kottayam(request):
    return render(request, "kottayam.html")


def pathanamthitta(request):
    return render(request, "pathanamthitta.html")


def thiruvananthapuram(request):
    return render(request, "thiruvananthapuram.html")


def palakkad(request):
    return render(request, "palakkad.html")


def kollam(request):
    return render(request, "kollam.html")


def kasargod(request):
    return render(request, "kasargod.html")


def malappuram(request):
    return render(request, "malappuram.html")


def kannur(request):
    return render(request, "kannur.html")


def kozhikode(request):
    return render(request, "kozhikode.html")


def button(request):
    return render(request, "button.html")


def message(request):
    return render(request, "message.html")


def registerations(request):
    district=['Districts.objects.all()']
    center=['Centers.objects.all()']
    if district==center:
        return center

    return render(request, "registerations.html", {'districts':district, 'centers': center})
