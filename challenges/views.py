from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
monthlyChallenges = {
    "january": "Workout everyday!!",
    "february": "Walk for 20 mins everyday!!",
    "march": "Learn to code 120 mins everyday!!",
    "april": "Workout everyday!!",
    "may": "go home early!",
    "june": "Stay git and learn fit",
    "july": "go to Canda",
    "august": "Workout everyday!!",
    "september": "Walk for 20 mins everyday!!",
    "october": "Learn to code 120 mins everyday!!",
    "november": "Workout everyday!!",
    "december": None,

}

# Creating the Index


def index(request):
    monthsList = list(monthlyChallenges.keys())

    return render(request, "challenges/index.html", {
        "listOfMonths": monthsList
    })


def monthly_challenge_by_number(request, monthNumber):
    monthsList = list(monthlyChallenges.keys())

    if monthNumber > len(monthsList):
        return HttpResponseNotFound("<h1>Invalid Month!</h1>")

    redirectMonth = monthsList[monthNumber - 1]
    # /challenge/january
    redirectPath = reverse("month-challenge", args=[redirectMonth])
    return HttpResponseRedirect(redirectPath)


def monthly_challenge(request, monthName):
    try:
        challenge_text = monthlyChallenges[monthName]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "monthName": monthName
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported!!</h1>")
