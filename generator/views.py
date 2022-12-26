from django.shortcuts import render
import random

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''

    lenght = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('-_+*#!$%&.='))
    if request.GET.get('numbers'):
        characters.extend(list('123467890'))    

    for x in range(lenght):
        
        generated_password += random.choice(characters)
        print(generated_password)

    return render(request, 'generator/password.html', {'password': generated_password})
    
def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

