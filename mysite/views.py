from django.http import HttpResponse, Http404
import datetime
from django.template import Template, Context
from django.template.loader import get_template


def hello(request):
    return HttpResponse("Hello world")


def my_homepage_view(request):
    return HttpResponse("This is the home page")


def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now.date()}))
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "In %s hour(s), it will be  %s." % (offset, dt)
    assert False
    return HttpResponse(html)


def ordering_notice(request):
    raw_template="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Ordering notice</title>
</head>
<body>
    <h1>Ordering notice</h1>

    <p>Dear {{ person_name }},</p>

    <p>Thanks for placing an order from {{ company }}. It's scheduled to ship on {{ s\
hip_date|date:"F j, Y" }}.</p>
    <p>Here are the items you've ordered:</p>
    <ul>
        {% for item in item_list %}
        <li>{{ item }}</li>{% endfor %}
    </ul>

    {% if ordered_warranty %}
    <p>Your warranty information will be included in the packaging.</p>
    {% else %}
    <p>
        You didn't order a warranty, so you're on your own when
        the products inevitably stop working.
    </p>
    {% endif %}

    <p>Sincerely,<br />{{ company }}</p>
</body>
</html>"""
    t = Template(raw_template)
    c = Context({'person_name': 'John Smith', 'company': 'Outdoor Equipment', 'ship_date': datetime.date(2015, 7, 2), 'ordered_warranty': False})
    print(t.render(c))
    return HttpResponse(t.render(c))