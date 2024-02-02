from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    Groups = Group.objects.all().values()
    count = Groups.count()
    Messages = []
    for x in Groups:
        Messages.append(x.Message_set.all())

    context = {'Groups': Groups,
               'count': count,
               'Messages': Messages}
    return render (request,'home.html',context)

def addInGroup(request):
    form = CreateInGroup()
    if request.method == 'POST':
        form = CreateInGroup(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render (request,'addInGroup.html',context)

def addInMessage(request):
    form = CreateInMessage()
    if request.method == 'POST':
        form = CreateInMessage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request,'addInMessage.html',context)

def addInMember(request):
    form = CreateInMember()
    if request.method == 'POST':
        form = CreateInMember(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request,'addInMember.html',context)
