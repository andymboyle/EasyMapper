from django.core import serializers
from django.http import HttpResponse as response

from sirensapi.models import Location


def json_full_feed(request):
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
