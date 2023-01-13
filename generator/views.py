from django.shortcuts import render
import random
from werkzeug.security import generate_password_hash
def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''

    lenght = int(request.GET.get('length'))

    if request.GET.get('special'):
        characters.extend(list('-_+*#!$%&.='))
    if request.GET.get('numbers'):
        characters.extend(list('123467890'))    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    for x in range(lenght):
        
        generated_password += random.choice(characters)
        
    password_encrypted = generate_password_hash(generated_password)
    #print(generated_password + password_encrypted)
    return render(request, 'generator/password.html', {'password': generated_password,'passwordsha256': password_encrypted})

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def recommendations(request):
    return render(request, 'generator/recommendations.html')

