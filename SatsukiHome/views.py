from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Messages
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({},request))

def music(request):
    template = loader.get_template('music.html')
    return HttpResponse(template.render({}, request))

def photo(request):
    template = loader.get_template('photo.html')
    return HttpResponse(template.render({}, request))

def message(request):
    template = loader.get_template('message.html')
    records = Messages.objects.all().values().order_by()
    context = {
        'records' : records,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    x = request.POST['username']
    y = request.POST['password']
    user = User.objects.create_user(x,"",y)
    user.save()
    return HttpResponseRedirect(reverse('index'))

@login_required
def leave(request):
    x = request.POST['word']
    y = request.POST['postname']
    newmessage = Messages(messages=x,owner=request.user,username=y)
    newmessage.save()
    return HttpResponseRedirect(reverse('message'))

# Create your views here.