from django.http import HttpResponse, Http404
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render



def hello(request):
    return HttpResponse("Hello world")


def my_homepage_view(request):
    return HttpResponse("This is the home page")


def current_datetime(request):
    now = datetime.datetime.now()
    # t = get_template('current_datetime.html')
    # html = t.render(Context({'current_date': now.date()}))
    # return HttpResponse(html)
    return render(request, 'current_datetime.html', Context({'current_date': now}))


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    next_time = datetime.datetime.now() + datetime.timedelta(hours=offset)
    c = Context({'hour_offset':offset, 'next_time':next_time})
    return render(request, 'hour_ahead.html', c)


def ordering_notice(request):
    c = Context({'person_name': 'John Smith', 'company': 'Outdoor Equipment', 'ship_date': datetime.date(2015, 7, 2), 'ordered_warranty': False})
    return render(request, 'letter.html', c)