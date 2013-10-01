from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse as response

from easymapper.models import Location


def locations(request):

    return render(request, 'index.html', {
        'locations': Location.objects.all(),
    })


def json_full_feed(request):
    """
    This is if you want to make an API of all of the data,
    but for this project we'll just be spitting it out onto
    a single page.
    """
    json_data = serializers.serialize(
        "json", Location.objects.all())

    resp = _cors_response(json_data)

    return resp


def _cors_response(content=None, status=200):
    resp = response()
    resp['Access-Control-Allow-Origin'] = '*'
    resp['Access-Control-Allow-Methods'] = 'POST, PUT, DELETE, OPTIONS'
    resp['Access-Control-Allow-Headers'] = 'Content-Type'
    resp['Content-Type'] = 'application/json'

    if content:
        resp.content = content

    if status:
        resp.status = status

    return resp
