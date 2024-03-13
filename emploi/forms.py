from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import *



class SignUpForm(UserCreationForm):
    e_mail = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'e_mail', 'password1', 'password2')


class CandidatureForm(forms.ModelForm):
    class Meta:
        model = Candidature
        fields = ['nom', 'prenom', 'e_mail', 'cv', 'lettre_motivation']

        cv = forms.FileField(label='CV')


class AnnonceForm(forms.ModelForm):

    class Meta:
        model = OffreEmploi
        fields = ['entreprise_name' ,'poste' ,'location' ,'description_entreprise' ,'mission', 'require_profil','user']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)