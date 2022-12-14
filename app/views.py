import datetime
import os
from audioop import reverse

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(requests):
    return HttpResponse("hello world!")

def time(requests):
    curtime = datetime.datetime.now().time()
    return HttpResponse(f'time = {curtime}')

def workdir(requests):
    file = os.listdir()
    qwe = f'список файлов: {file}'
    return HttpResponse(qwe)


