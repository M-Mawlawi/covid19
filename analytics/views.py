from django.shortcuts import render
from django.http import HttpResponse
import requests,json
import dload
from django.utils.safestring import SafeString
from .getapi import getdata

def index(request):
    getdata.get()
    response = open('C:/Users/Mehmet/Desktop/COVID19/covid19/data.json')
    responses = json.load(response)
    curl = 'https://pkgstore.datahub.io/core/country-list/data_json/data/8c458f2d15d9f2119654b29ede6e45b8/data_json.json'
    flag = dload.json(curl)
    return render(request,"index.html",{"response":responses,"flag":flag})
