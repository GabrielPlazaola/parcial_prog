from django.shortcuts import get_list_or_404, render

import requests
import json

from django.http import HttpResponse
from django.template import loader



response = requests.get("http://api.citybik.es/v2/networks")


api = response.json()


def index(request):
    context = {'api': api}
    return render(request, 'api.html', context)
