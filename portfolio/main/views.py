import json
import os
from datetime import datetime

from django.conf import settings
from django.shortcuts import render


def age():
    date_de_naissance = datetime(2002, 7, 31)
    date_actuelle = datetime.now()
    return date_actuelle.year - date_de_naissance.year - (
                (date_actuelle.month, date_actuelle.day) < (date_de_naissance.month, date_de_naissance.day))


# Create your views here.

def get_data(lang):
    filename = os.path.join(settings.BASE_DIR, 'main/static/main/fixtures/' + lang + '_content.json')
    with open(filename, "r", encoding='utf-8') as f:
        data = json.load(f)
    return data


def home(request):
    if request.GET.get('lang') == 'en' or request.GET.get('lang') == 'EN':
        lang = 'en'
    else:
        lang = 'fr'
    data = get_data(lang)

    return render(request, 'main/home.html', {'data': data, 'age': age, 'lang': lang})


def cv(request):
    if request.GET.get('lang') == 'en' or request.GET.get('lang') == 'EN':
        lang = 'en'
    else:
        lang = 'fr'
    data = get_data(lang)
    return render(request, 'main/cv.html', {'data': data, 'age': age, 'lang': lang})


def contact(request):
    if request.GET.get('lang') == 'en' or request.GET.get('lang') == 'EN':
        lang = 'en'
    else:
        lang = 'fr'
    data = get_data(lang)
    return render(request, 'main/contact.html', {'data': data, 'age': age, 'lang': lang})


def projets(request):
    if request.GET.get('lang') == 'en' or request.GET.get('lang') == 'EN':
        lang = 'en'
    else:
        lang = 'fr'
    data = get_data(lang)
    return render(request, 'main/projets.html', {'data': data, 'age': age, 'lang': lang})
