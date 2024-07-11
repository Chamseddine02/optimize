import datetime

from .models import *
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index_company(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    print(html)
    return HttpResponse(html)


def store(request, id):
    now = datetime.datetime.now()
    Lockers = Locker.objects.filter(id=id)
    return render(request, "store.html", {"lockers": Lockers})
