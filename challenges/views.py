from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for at least 20 minutes every day",
    "march": "Learn Django for at least 20 minutes every day",
    "april": "Eat no meat for the entire month",
    "may": "Walk for at least 20 minutes every day",
    "june": "Learn Django for at least 20 minutes every day",
    "july": "Eat no meat for the entire month",
    "august": "Walk for at least 20 minutes every day",
    "september": "Learn Django for at least 20 minutes every day",
    "october": "Eat no meat for the entire month",
    "november": "Walk for at least 20 minutes every day",
    "december": None
}

def chanllenges_list(request):
    list_item = ""
    months = monthly_challenges.keys()
    for month in months:
        month = month
        month_path = reverse("month-challenge", args=[month])
        list_item += f"<li><a href='{month_path}'>{month.capitalize()}</a></li>"
    monthslist = f"<ul>{list_item}</ul>"
        
    
    return render(request, "challenges/index.html", {
        "months": months
    })
    

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenges/<str:month>
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        chanllenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": chanllenge_text,
            "month": month.capitalize()
        })
    except:
        raise Http404()