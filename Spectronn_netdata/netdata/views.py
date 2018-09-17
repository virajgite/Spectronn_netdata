from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from registration.views import RegistrationView


# Create your views here.

@login_required
def index(request):
	if request.method=="GET":
		context={ }
		template=loader.get_template('netdata/index.html')
		return HttpResponse(template.render(context,request))
	if request.method=="POST":
		context={ }
		template=loader.get_template('netdata/index.html')
		return HttpResponse(template.render(context,request))

@login_required
def historic(request):
	if request.method=="GET":
		context={}
		template=loader.get_template('netdata/historic.html')
		return HttpResponse(template.render(context,request))
	if request.method=="POST":
		context={}
		template=loader.get_template('netdata/historic.html')
		return HttpResponse(template.render(context,request))

@login_required
def pie(request):
        if request.method=="GET":
                context={}
                template=loader.get_template('netdata/pie.html')
                return HttpResponse(template.render(context,request))
        if request.method=="POST":
                context={}
                template=loader.get_template('netdata/pie.html')
                return HttpResponse(template.render(context,request))
		
