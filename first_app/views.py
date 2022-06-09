from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date


def hellodjango(requests: HttpRequest):
    return HttpResponse("Hello Django!!")


def func_name(request, name):
    return HttpResponse(f'Hello {name}')


hw = date(2022, 3, 22)


def date_hw(request):
    return HttpResponse(hw)


def date_year(request):
    return HttpResponse(hw.year)


def date_month(request):
    return HttpResponse(hw.month)


def date_day(request):
    return HttpResponse(hw.day)
