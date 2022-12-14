import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Cloth, Cloth3
# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
import math
import requests
import json


def index(request):
    return render(request, 'text/index.html')


def s1(request):
    return render(request, 'text/s1.html')


def s2(request):
    return render(request, 'text/s2.html')


def s3(request):
    return render(request, 'text/s3.html')


'''def s4(request):
    return render(request, 'text/s4.html')


def s4_1(request):
    return render(request, 'text/s4_1.html')


def s4_2(request):
    return render(request, 'text/s4_2.html')


def s4_3(request):
    return render(request, 'text/s4_3.html')


def s4_4(request):
    return render(request, 'text/s4_4.html')


def s4_5(request):
    return render(request, 'text/s4_5.html')


def s4_6(request):
    return render(request, 'text/s4_6.html')


def s4_7(request):
    return render(request, 'text/s4_7.html')


def s4_8(request):
    return render(request, 'text/s4_8.html')


def s4_9(request):
    return render(request, 'text/s4_9.html')'''


def s5(request):
    return render(request, 'text/s5.html')


def s6(request):
    return render(request, 'text/s6.html')


def s7(request):
    return render(request, 'text/s7.html')


def text(request, question_id):
    question = get_object_or_404(Cloth, pk=question_id)
    return render(request, 'text/text.html', {'question': question})


def textva(request, question_id):
    question = get_object_or_404(Cloth, pk=question_id)

    question.is_used = True
    question.save()

    return HttpResponseRedirect(reverse('text:ans', args=(question.id,)))


def textvb(request, question_id):
    question = get_object_or_404(Cloth, pk=question_id)

    question.is_used = False
    question.save()

    return HttpResponseRedirect(reverse('text:ans', args=(question.id,)))


def ans(request, question_id):
    question = get_object_or_404(Cloth, pk=question_id)
    return render(request, 'text/ans.html', {'question': question})


def textcollect(request):
    question = Cloth.objects.order_by()
    return render(request, 'text/textcollect.html', {'question': question})


def text2(request, question_id):
    question = get_object_or_404(Cloth3, pk=question_id)
    return render(request, 'text/text2.html', {'question': question})


def textva2(request, question_id):
    question = get_object_or_404(Cloth3, pk=question_id)

    question.is_used = True
    question.save()

    return HttpResponseRedirect(reverse('text:ans2', args=(question.id,)))


def textvb2(request, question_id):
    question = get_object_or_404(Cloth3, pk=question_id)

    question.is_used = False
    question.save()

    return HttpResponseRedirect(reverse('text:ans2', args=(question.id,)))


def ans2(request, question_id):
    question = get_object_or_404(Cloth3, pk=question_id)
    return render(request, 'text/ans2.html', {'question': question})


def textcollect2(request):
    question = Cloth3.objects.order_by()
    return render(request, 'text/textcollect2.html', {'question': question})


def tenki_show(request):
    message = "?????????????????????????????????\n???) ??????"
    context = {
        'message': message
    }
    return render(request, 'text/tenki.html', context)


def move_to_gamepage(request):
    apiKey = "fa5524d5e12279c70853e85627fd0e0e"
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"

    # URL??????
    completeUrl = baseUrl + "appid=" + apiKey + \
        "&q=" + request.GET.get('player1') + "&lang=ja"

    # ???????????????
    response = requests.get(completeUrl)

    # ???????????????????????????JSON????????????????????????Python???????????????????????????
    cityData = response.json()
    # players = {
    #    'player1': request.GET.get('player1'),
    #    'player2': request.GET.get('player2'),
    #    'player3': request.GET.get('player3'),
    # }

    try:
        players = {
            'player1': cityData["name"],
            'player2': cityData["weather"][0]["description"],
            'player3': math.floor(cityData["main"]["temp"] - 273.15),
            'player4': math.floor(cityData["main"]["temp_max"] - 273.15),
            'player5': math.floor(cityData["main"]["temp_min"] - 273.15),
            'player6': cityData["main"]["humidity"],
            'player7': cityData["main"]["pressure"],
            'player8': cityData["wind"]["speed"]
        }
        return render(request, 'text/game_page.html', players)

    except:
        message = "??????????????????????????????????????????????????????\n??????????????????????????????????????????\n?????????????????????????????????\n???) ??????"
        context = {
            'message': message
        }
        return render(request, 'text/tenki.html', context)


def divi(request):
    message = "??????????????????????????????????????????\n???) ??????"
    context = {
        'message': message
    }
    return render(request, 'text/divi.html', context)


def move_to_div(request):

    date = datetime.datetime.today().strftime("%Y/%m/%d")

    # http://api.jugemkey.jp/api/horoscope/year/month/day ?????????
    res = requests.get(url='http://api.jugemkey.jp/api/horoscope/free/' + date)
    idea = request.GET.get('player1')

    #apiKey = "fa5524d5e12279c70853e85627fd0e0e"
    #baseUrl = "http://api.openweathermap.org/data/2.5/weather?"

    # URL??????
    # completeUrl = baseUrl + "appid=" + apiKey + \
    #   "&q=" + request.GET.get('player1') + "&lang=ja"

    # ???????????????
    #response = requests.get(completeUrl)

    # ???????????????????????????JSON????????????????????????Python???????????????????????????
    #cityData = response.json()
    # players = {
    #    'player1': request.GET.get('player1'),
    #    'player2': request.GET.get('player2'),
    #    'player3': request.GET.get('player3'),
    # }
    for i in range(12):
        if(idea == res.json()["horoscope"][date][i]['sign']):
            count = i
            break

    try:
        players = {
            'player1': res.json()["horoscope"][date][count]["content"],
            'player2': res.json()["horoscope"][date][count]["item"],
            'player3': res.json()["horoscope"][date][count]["money"],
            'player4': res.json()["horoscope"][date][count]["total"],
            'player5': res.json()["horoscope"][date][count]["job"],
            'player6': res.json()["horoscope"][date][count]["color"],
            'player7': res.json()["horoscope"][date][count]["day"],
            'player8': res.json()["horoscope"][date][count]["love"],
            'player9': res.json()["horoscope"][date][count]["rank"],
            'player10': res.json()["horoscope"][date][count]["sign"],
        }
        return render(request, 'text/div_page.html', players)

    except:
        message = "??????????????????????????????????????????????????????\n???????????????????????????????????????"
        context = {
            'message': message
        }
        return render(request, 'text/divi.html', context)
