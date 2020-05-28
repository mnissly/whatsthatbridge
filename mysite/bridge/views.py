from django.http import HttpResponse
from django.urls import path
from django.template import loader
from .models import  Bridge
from .scraping import get_bridgehunters_page, parse_page, county_list


def index(request):
    template = loader.get_template('bridge/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def dataloader(request):
    template = loader.get_template('bridge/dataloader.html')
    context = {}
    return HttpResponse(template.render(context, request))

def detail(request, bridge_id):
    return HttpResponse("You're looking at bridge %s." % bridge_id)

def add_county(request):
    #county_text = request.POST['county_text']
    #question = Bridge(question_text=question_text, pub_date=timezone.now())
    #question.save()
    #return HttpResponseRedirect(reverse('polls:index'))

    county_url = 'https://bridgehunter.com/md/list/'
    url = 'https://bridgehunter.com'
    counties = county_list(county_url)
    for county in counties:
        print(f'{url=},{county=}')
        bh_page = get_bridgehunters_page(url,county)
        parse_page(bh_page)

    return HttpResponse("The data is in the database")

