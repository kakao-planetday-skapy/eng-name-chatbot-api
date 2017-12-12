import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from api.nameParser import NameParser


@csrf_exempt
def random(request):
    parser = NameParser()
    return JsonResponse(parser.callAnyName(), safe=False)


@csrf_exempt
def getName(request):
    name = json.loads(request.body)['userRequest']['utterance']
    if name is None:
        return JsonResponse({}, safe=False)
    name = name.replace(" 이 이름 검색해줘", "")
    parser = NameParser()
    return JsonResponse(parser.callByEnglishName(name), safe=False)
