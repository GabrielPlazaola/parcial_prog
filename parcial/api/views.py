from django.shortcuts import get_list_or_404, render

import requests
import json

from django.http import HttpResponse
from django.template import loader


respuestaprincipal = requests.get("https://www.cultura.gob.ar/api/v2.0/?format=json")
apiprincipal = respuestaprincipal.json()


response = requests.get(apiprincipal['organismos'])
response2 = requests.get(apiprincipal['programas'])
response3 = requests.get(apiprincipal['museos'])
response4 = requests.get(apiprincipal['institutos'])
response5 = requests.get(apiprincipal['tramites'])
response6 = requests.get(apiprincipal['convocatorias'])

api = response.json()
api2 = response2.json()
api3 = response3.json()
api4 = response4.json()
api5 = response5.json()
api6 = response6.json()

def index(request):
    context = {'api': api, 'api2': api2, 'api3': api3, 'api4': api4, 'api5': api5, 'api6': api6}
    return render(request, 'api.html', context)
