from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from api.nameParser import NameParser


def random(request):
    parser = NameParser()
    return JsonResponse(parser.callAnyName(), safe=False)


def getName(request,name):
    parser = NameParser()
    return JsonResponse(parser.callByEnglishName(name), safe=False)