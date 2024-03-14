from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.views.generic import ListView, DetailView, CreateView, View
from django.views.generic.edit import FormView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class HomeView (ListView):
    model = OffreEmploi
    template_name = 'emploi/home.html'
    context_object_name = 'post'



class InscriptionView(FormView):
    template_name = 'registration/inscription.html'
    form_class = SignUpForm

    def form_valid(self, form):
        member = form.save(commit=False)
        member.user = self.request.user
        member.save()
        return redirect('home')
    
    def get(self, request, *args, **kwargs):
        form = self.get_form()
        return self.render_to_response(self.get_context_data(form=form))


class OffreEmploiDetailView(DetailView):
    model = OffreEmploi
    template_name = 'emploi/offre_emploi.html'
    context_object_name = 'post'



class CandidatureCreateView(CreateView):
    model = Candidature
    # form_class = CandidatureForm
    template_name = 'emploi/candidature.html'
    fields = ['nom', 'prenom', 'e_mail', 'cv', 'lettre_motivation']

    def form_valid(self, form):
        post = OffreEmploi.objects.get(id=self.kwargs['pk'])
        application = form.save(commit=False)
        application.offre_emploi = post
        application.pub_date = timezone.now()
        application.user = self.request.user
        application.save()
        return redirect('success', pk=self.kwargs['pk'])



from django.views import generic

class SuccessView(generic.TemplateView):
    template_name = 'emploi/success.html'




class AnnonceFormView(LoginRequiredMixin,FormView):
    model = OffreEmploi
    form_class = AnnonceForm
    template_name = 'emploi/annonce.html'
    success_url = reverse_lazy('home')

    def form_valid(self,form):
        offre = form.save()
        offre.user = self.request.user
        offre.pub_date = timezone.now()
        offre.save()
        return redirect(reverse('home'))



class ConnectionFormView(FormView):
    form_class = LoginForm
    template_name = 'registration/connection.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user:
            login(self.request, user)    
            return redirect('home')
        return super().form_valid(form)
    
    #Methode pour gerer la requete GET et initialiser le formulaire
    def get(self, request, *args, **kwargs):
        form = self.get_form()
        return self.render_to_response(self.get_context_data(form=form))


class DeconnectionView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('connection')