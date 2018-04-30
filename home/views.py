from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")


def detail(request, question_id):
    return HttpResponse("You're looking at <strong>question</strong> %s." % question_id)


def results(request, question_id):
    response = "You're looking at the <strong>results</strong> of question %s."
    return HttpResponse(response % question_id)
