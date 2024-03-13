from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.views.generic import ListView
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

class HomeView (ListView):
    model = OffreEmploi
    template_name = 'emploi/home.html'
    context_object_name = 'post'



def Inscription(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.user = request.user
            member.save()
            return redirect('home')  # Redirige vers une autre page après l'inscription réussie
    else:
        form = SignUpForm()
    
    return render(request, 'registration/inscription.html', {'form': form})


def offre_emploi(request, pk):
    post = OffreEmploi.objects.get(id=pk)
    return render (request, 'emploi/offre_emploi.html', {'post':post,})



def candidature(request, pk):
    post = OffreEmploi.objects.get(id=pk)

    if request.method == 'POST':
        form = CandidatureForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.offre_emploi = post
            application.pub_date = timezone.now()
            application.user = request.user
            application.save()
            print('sa marche')
            return redirect(reverse('success', kwargs={'pk': pk} ))
    else:
        form = CandidatureForm(initial={'offre_emploi': post})
    return render(request, 'emploi/candidature.html', {'form': form, 'post': post})



from django.views import generic

class SuccessView(generic.TemplateView):
    template_name = 'emploi/success.html'


@login_required
def annonce(request):
    if request.method == 'POST':
        form = AnnonceForm(request.POST)
        if form.is_valid():
            offre = form.save()
            offre.user = request.user
            offre.pub_date = timezone.now()
            offre.save()
            print('sa marche')
            return redirect(reverse('home'))
    else:
        form = AnnonceForm()
    return render(request, 'emploi/annonce.html', {'form':form})



# login page
def connection(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'registration/connection.html', {'form': form})


# logout page
def deconnection(request):
    logout(request)
    return redirect('connection')