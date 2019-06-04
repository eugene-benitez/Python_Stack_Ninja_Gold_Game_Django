from django.shortcuts import render, HttpResponse, redirect

from datetime import datetime
import random

list = []


def index(request):
    request.session['gold'] = 0
    return render(request, "ninja_gold/index.html")


def farm(request):
    current = datetime.now()
    loc = "Farm"
    added_gold = random.randint(10, 20)
    request.session['gold'] += added_gold
    statement = f"Earned {added_gold} from the Farm! ({current})"
    list.append(statement)
    context = {
        "current_time": current,
        "added": added_gold,
        "location": loc,
        "lists": list,
    }
    return render(request, "ninja_gold/index.html", context)


def cave(request):
    current = datetime.now()
    loc = "Cave"
    added_gold = random.randint(5, 10)
    request.session['gold'] += added_gold
    statement = f"Earned {added_gold} from the Cave! ({current})"
    list.append(statement)
    context = {
        "current_time": current,
        "added": added_gold,
        "location": loc,
        "statements": statement,
        "lists": list,
    }
    return render(request, "ninja_gold/index.html", context)


def house(request):
    current = datetime.now()
    loc = "House"
    added_gold = random.randint(2, 5)
    request.session['gold'] += added_gold
    statement = f"Earned {added_gold} from the House! ({current})"
    list.append(statement)
    context = {
        "current_time": current,
        "added": added_gold,
        "location": loc,
        "statements": statement,
        "lists": list,
    }
    return render(request, "ninja_gold/index.html", context)


def casino(request):
    current = datetime.now()
    loc = "Casino"
    added_gold = random.randint(-50, 50)
    if added_gold < 0:
        statement = f"Entered a Casino and lost {added_gold} ... Ouch. ({current}) "
    else:
        statement = f"Earned {added_gold} from the Casino! ({current})"

    list.append(statement)
    request.session['gold'] += added_gold

    context = {
        "current_time": current,
        "added": added_gold,
        "location": loc,
        "statements": statement,
        "lists": list,
    }
    return render(request, "ninja_gold/index.html", context)
