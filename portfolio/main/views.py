from django.shortcuts import render
import json, os
from django.conf import settings
# Create your views here.

def get_data(lang):
    filename = os.path.join(settings.BASE_DIR, 'main/static/main/fixtures/texte.json')
    with open(filename, "r", encoding='utf-8') as f:
        data = json.load(f)
    return data[lang]

def home(request):
    if request.GET.get('lang') == 'en' or request.GET.get('lang') == 'EN':
        lang = 'en'
    else:
        lang = 'fr'
    data = get_data(lang)

    return render(request, 'main/home.html', {'data': data, 'age':20, 'lang' : lang})

def cv(request):
    if request.GET.get('lang') == 'en' or request.GET.get('lang') == 'EN':
        lang = 'en'
    else:
        lang = 'fr'
    data = get_data(lang)
    return render(request, 'main/cv.html', {'data': data, 'age':20, 'lang' : lang})

def contact(request):
    if request.GET.get('lang') == 'en' or request.GET.get('lang') == 'EN':
        lang = 'en'
    else:
        lang = 'fr'
    data = get_data(lang)
    return render(request, 'main/contact.html', {'data': data, 'age':20, 'lang' : lang})

def projets(request):
    if request.GET.get('lang') == 'en' or request.GET.get('lang') == 'EN':
        lang = 'en'
    else:
        lang = 'fr'
    data = get_data(lang)
    return render(request, 'main/projets.html', {'data': data, 'age':20, 'lang' : lang})