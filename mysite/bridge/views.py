from django.http import HttpResponse
from django.urls import path
from django.template import loader
from . import views


def index(request):
    template = loader.get_template('bridge/index.html')
    return HttpResponse(template)


def detail(request, bridge_id):
    return HttpResponse("You're looking at bridge %s." % bridge_id)
