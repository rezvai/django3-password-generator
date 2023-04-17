from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    thepassword = ""
    characters = list("abcdefghijklmnopqrstuvwxyz")
    length = request.GET.get('length', 12)
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    for i in range(int(length)):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})


def information(request):
    return render(request, 'generator/information.html')
