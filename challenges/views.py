from calendar import month
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound, HttpResponseRedirect

monthly_challenge = {
    'january':'This is my first views',
    'feburary':'This is februray Month and we should try to Improve our skills',
    'march': 'learn Django every 20 mins in a day',
    'april':'Eat Healthy',
    'may':'Eat Healthy2',
    'june': 'learn Django every 20 mins in a day',
    'july':'This is februray Month and we should try to Improve our skills',
    'august': 'learn Django every 20 mins in a day',
    'september': 'learn Django every 20 mins in a day',
    'november':'This is my second views',
    'december':'This is my third views',
}

# Create your views here.


def monthly_challenges_by_number(request,month):
    try:
        monthly_challenges_text = list(monthly_challenge.keys())
        forward_month = monthly_challenges_text[month]

        return HttpResponseRedirect('/challenges/'+ forward_month)
    except:
        return HttpResponseNotFound('This is not supported..!')

def monthly_challenges(request,month):
    try:
        monthly_challenges_text = monthly_challenge[month]
        return HttpResponse(monthly_challenges_text)
    except:
        return HttpResponseNotFound("This is not Supported")
    
