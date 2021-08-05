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
    curl = 'https://restcountries.eu/rest/v2/all'
    flag = dload.json(curl)
    return render(request,"index.html",{"response":responses,"flag":flag})
