
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from time import strftime, gmtime
from random import *

def index(request):
	if "count" not in request.session:
		request.session["count"] = []
	if "total" not in request.session:
		request.session["total"] = 0
	context = {
		"time": strftime("%H:%M %p %Y-%m-%d", gmtime())
	}
	return render(request, "ninja/index.html", context)

def farm(request):
	g = randint(10,20)
	n = "Farm!"
	c = "green"
	request.session["count"] += [{'gold': g, "name": n, "color": c}]
	request.session["total"] += g
	return redirect("/")

def cave(request):
	g = randint(5,10)
	n = "Cave!"
	c = "green"
	request.session["count"] += [{'gold': g, "name": n, "color": c}]
	request.session["total"] += g
	return redirect("/")

def house(request):
	g = randint(2,5)
	n = "House!"
	c = "green"
	request.session["count"] += [{'gold': g, "name": n, "color": c}]
	request.session["total"] += g
	return redirect("/")

def casino(request):
	g = randint(-50,50)
	n = "Casino!"
	if g >= 0:
		c = "green"
		n = "Casino!"
	else:
		c = "red"
		n = "casino, ouch...."
	request.session["count"] += [{'gold': g, "name": n, "color": c}]
	request.session["total"] += g 
	return redirect("/")
























# def update(request):
# 	if "name" not in request.POST:
# 		n = "No name chosen"
# 		request.session["name"] = "No name chosen"

# 	else:
# 		request.session['name'] = request.POST["name"]
# 		n = request.session['name']

	
# 	if "colors" not in request.POST:
# 		c = "No color chosen"
# 		request.session["colors"] = "No color chosen"

# 	else:
# 		request.session['colors'] = request.POST["colors"]
# 		c = request.session['colors']

# 	if "BIG" not in request.POST:
# 		request.session["BIG"] = "Big not chosen"
# 		b = "20px"
# 	else:
# 		request.session['BIG'] = request.POST["BIG"]
# 		b = "50px"

# 	print("*"*100)
# 	request.session["word"] +=[{'name': n, 'color': c, 'big': b}]
# 	print(request.session['word'])
# 	return redirect("/")

# def clear(request):
# 	print("CLEAR "*40)
# 	request.session['word'] = []
# 	request.session["name"] = []
# 	return redirect("/")




