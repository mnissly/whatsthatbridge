from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import path
from django.template import loader
from django.views import generic

from . import views
from .models import Bridge
from .scraping import get_bridgehunters_page, parse_page


def index(request):
    template = loader.get_template('bridge/index.html')
    random = Bridge.objects.order_by("?").first
    context = {'random': random}
    return HttpResponse(template.render(context, request))


def detail(request, bridge_id):
    bridge = get_object_or_404(Bridge, pk=bridge_id)
    return render(request, 'bridge/detail.html', {'bridge': bridge})


def add_county(request):
    county_text = request.POST['county_text']
    # question = Bridge(question_text=question_text, pub_date=timezone.now())
    # question.save()
    # return HttpResponseRedirect(reverse('polls:index'))
    bh_page = get_bridgehunters_page(county_text)
    parse_page(bh_page)
    return HttpResponse(Bridge)
