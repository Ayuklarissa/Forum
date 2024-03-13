from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView
from django.urls import reverse


# Create your views here.
def home(request):
    nbr_groups = Group.objects.count() 
    nbr_members = Member.objects.count()
    nbr_messages = Message.objects.count() 
    latest_messages = Message.objects.filter(sujet__isnull=True).order_by('-pub_date') [:10]
    context = {
        'nbr_members': nbr_members,
        'nbr_groups': nbr_groups,
        'nbr_messages': nbr_messages,
        'latest_messages': latest_messages,
    }
    return render(request, 'Discussion/home.html', context)


def groupe(request):
    groups = Group.objects.all()
    context = {
        'groups': groups,
    }
    return render(request, 'Discussion/groupe.html', context)


def liste(request, pk):
    groups = Group.objects.get(id=pk)
    group_member = groups.members.all()
    # notgroupmember_list = Member.objects.exclude(group__id=pk)
    context = {
        'groups': groups,
        'group_member': group_member
    }
    return render (request, 'Discussion/liste.html',context)


def not_member(request, pk):
    group = Group.objects.get(id=pk)
    notgroupmember = Member.objects.exclude(group__id=pk)
    context = {
        'groups': group,
        'notgroupmember': notgroupmember
    }
    return render (request, 'Discussion/not_member.html',context)


def question(request, pk):
    groups = Group.objects.get(id=pk)
    groupe_messages = Message.objects.filter(sujet__isnull=True, groupe=groups)
    context = {
        'group': groups,
        'groupe_messages': groupe_messages
    }
    return render(request, 'Discussion/question.html', context)


def repondre(request, pk, pk_question):
    # messages = Message.objects.all()
    question = Message.objects.get(id=pk_question)
    messages = Message.objects.filter(sujet=question)
    group = Group.objects.get(id=pk)
    groupe_messages = Message.objects.filter(sujet__isnull=True, groupe=group)
    
    context = {
        'question': question,
        # 'reponses': reponses,
        'messages': messages,
        'group':group ,
        'groupe_messages': groupe_messages,
    }
    return render(request, 'Discussion/repondre.html', context)


def respond_to_question(request, pk_question):
    
    if request.method == 'POST':
        form = respond_to_questionForm(request.POST)
        if form.is_valid():
            reponse = form.save(commit=False)   
            reponse.pub_date = timezone.now()
            reponse.member = Member.objects.get(user=request.user)
            reponse.save()
            print('sa marche')
            return redirect(reverse('repondre', kwargs={'pk_question': pk_question, 'pk': reponse.groupe.pk} ))
        else:
            # request.mess
            print(form.errors.as_data())
            return (reverse('repondre', kwargs={'pk_question': pk_question}))
    else:
        return (reverse('repondre', kwargs={'pk_question': pk_question}))
    

def add_member(request,pk,pk_membre):
    if request.method == 'POST':
        form = AddMemberForm(request.POST)
        if form.is_valid():
            membre = form.save(commit=False)
            membre.group = Group.objects.get(id=pk)
            membre.member = Member.objects.get(id=pk_membre)
            membre.group.members.add(membre.member)
            membre.save()
            print('ca marche')
            return redirect(reverse ('not_member', kwargs={'pk_membre': pk_membre , 'pk':pk}))  # Rediriger vers la page de liste des membres après l'ajout
        else:
            print(form.errors.as_data())
            return(reverse ('not_member', kwargs={'pk_membre': pk_membre , 'pk':pk}))
    else:
        return(reverse ('not_member', kwargs={'pk_membre': pk_membre , 'pk':pk}))

    

# def AddMemberView(request, pk):
#     if request.method == 'POST':
#         form = AddMemberForm(request.POST)
#         if form.is_valid():
#             member = form.save()  # Enregistre le membre dans la base de données
#             group = Group.objects.get(id=pk)  # Récupère le groupe existant
#             group.members.add(member)  # Ajoute le membre au groupe
#             return redirect('liste')  # Redirige vers une page de succès ou une autre page souhaitée après l'ajout du membre
#     else:
#         form = AddMemberForm()
    
#     return render(request, 'not_member.html', {'form': form})


def SignUpView(request):
    if request.method == 'POST':
        form = SignUpViewForm(request.POST)
        if form.is_valid():
            user = form.save()
            member = Member(user=user,e_mail=user.email,name=user.username)
            member.save()
            return redirect('home')  # Redirige vers une autre page après l'inscription réussie
    else:
        form = SignUpViewForm()
    
    return render(request, 'registration/signup.html', {'form': form})









































































































































# def addInGroup(request):
#     form = CreateInGroup()
#     if request.method == 'POST':
#         form = CreateInGroup(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context = {'form':form}
#     return render (request,'ajouterGroup.html',context)

# def addInMessage(request):
#     form = CreateInMessage()
#     if request.method == 'POST':
#         form = CreateInMessage(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context ={'form':form}
#     return render(request,'ajouterMessage.html',context)

# def addInMember(request):
#     form = CreateInMember()
#     if request.method == 'POST':
#         form = CreateInMember(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context ={'form':form}
#     return render(request,'ajouterMember.html',context)


# def ajouter_message(request, pk):
#     groups = Group.objects.get(id=pk)
#     message = Message.objects.filter(sujet__isnull=True)
#     form = Ajouter_message()
#     if request.method == 'POST':
#         form = Ajouter_message(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context = {
#         'form':form,
#         'message': message,
#         'group': groups
#     }
#     return render(request, 'Discussion/ajouter_message.html', context)

















# R

# 