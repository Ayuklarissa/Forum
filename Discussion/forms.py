from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import *


class SignUpViewForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class respond_to_questionForm(forms.ModelForm):

    class Meta:
        model= Message
        fields = ['message_text', 'sujet', 'groupe']


class AddMemberForm (forms.ModelForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta:
        model = Member
        fields = ['name', 'e_mail', 'group']

