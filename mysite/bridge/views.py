from django.http import HttpResponse
from django.urls import path
from django.template import loader
from django.views import generic

from . import views
from .models import Bridge
from .scraping import get_bridgehunters_page, parse_page


def index(request):
    template = loader.get_template('bridge/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


class DetailView(generic.DetailView):
    model = Bridge
    template_name = "bridge/detail.html"


def add_county(request):
    county_text = request.POST['county_text']
    # question = Bridge(question_text=question_text, pub_date=timezone.now())
    # question.save()
    # return HttpResponseRedirect(reverse('polls:index'))
    bh_page = get_bridgehunters_page(county_text)
    parse_page(bh_page)
    return HttpResponse(Bridge)
