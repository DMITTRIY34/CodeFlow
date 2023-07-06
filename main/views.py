from django.http import HttpResponseNotFound
from django.shortcuts import render, HttpResponse

from .models import *

#card = ["Копирование", "Вставка", "Меню", "Поиск"]

def index(request):
    card = Card.objects.all()
    return render(request, 'main/index.html', {
        'title':'CodeFlow',
        'card' : card
    })

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Ошибка 404</h1>Страница не найдена")
