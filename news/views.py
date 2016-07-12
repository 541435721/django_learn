from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("hello world")
    dic = {"article_list": ["1", "2", "3"]}
    return render(request, 'index.html', dic)
