# Commandes pour creer un nouveau groupe:
from Discussion.models import Group
from django.utils import timezone
g = Group(name="ENJ", topic="Entre Nous Jeunes", description="Ici on est free", date_created=timezone.now()) 
g.save()
g = Group(name="IT-Develop", topic="Spring-Django-Node.js", description="Everything you need to know about Software develop", date_created=timezone.now())
g.save()
g = Group(name="MODE", topic="All-FASHION", description="Here we talk only about what is in Trend", date_created=timezone.now())
g.save()

#Commandes pour avoir tout les objets de la classe Group:
Group.objects.all().values()

#Pour recuperer un objet selon un attribut:
Group.objects.get(id=2)

#Pour Creer un utilisateur:
from django.contrib.auth.models import User
user = User.objects.create_user('lari', password='cliff')
user.is_superuser = True
user.is_staff = True
user.save()

#Pour creer une instance de User:
User1=User.objects.get(id=1)

#Pour creer un nouveau membre:
from Discussion.models import Member
member = Member (name='lari', e_mail='lari@gmail.com', role='Administrator', date_inscription=timezone.now(), user=User)
member.save()


# Pour creer plusieur Users a la fois:
from django.contrib.auth.models import User
users = [
    {'username': 'utilisateur21', 'password': 'motdepasse1'},
    {'username': 'utilisateur22', 'password': 'motdepasse2'},
    {'username': 'utilisateur23', 'password': 'motdepasse3'},
    {'username': 'utilisateur24', 'password': 'motdepasse4'},
    {'username': 'utilisateur25', 'password': 'motdepasse5'},
    {'username': 'utilisateur26', 'password': 'motdepasse6'},
    {'username': 'utilisateur27', 'password': 'motdepasse7'},
    {'username': 'utilisateur28', 'password': 'motdepasse8'},
    {'username': 'utilisateur29', 'password': 'motdepasse9'},
    {'username': 'utilisateur30', 'password': 'motdepasse10'},
    {'username': 'utilisateur31', 'password': 'motdepasse11'},
    {'username': 'utilisateur32', 'password': 'motdepasse12'},
    {'username': 'utilisateur33', 'password': 'motdepasse13'},
    {'username': 'utilisateur34', 'password': 'motdepasse14'},
    {'username': 'utilisateur35', 'password': 'motdepasse15'},
    {'username': 'utilisateur36', 'password': 'motdepasse16'},
    {'username': 'utilisateur37', 'password': 'motdepasse17'},
    {'username': 'utilisateur38', 'password': 'motdepasse18'},
    {'username': 'utilisateur39', 'password': 'motdepasse19'},
    {'username': 'utilisateur0', 'password': 'motdepasse20'},
]
for user_data in users:
    user = User.objects.create_user(username=user_data['username'], password=user_data['password'])
    user.save()

#Pour Creer des membres associes aux users:
from django.contrib.auth.models import User
from Discussion.models import Member
users = User.objects.all()
for user in users:
    member = Member(user=user, first_name="John", last_name="Doe")
    member.save()


# Vérifier si le membre fait partie du groupe
if Member in Group.members.all():
    print(f"Le membre {Member.name} fait partie du groupe {Group.name}.")
else:
    print(f"Le membre {Member.name} ne fait pas partie du groupe {Group.name}.")

#Pour Afficher tout les membres d'un groupe
## Récupérer tous les membres du groupe
group1=Group.objects.values(id=1)
Group_members = group1.members.all()
## Afficher les membres du groupe
for Member in Group_members:
    print(Member.name)

#Pour creer un message
from Discussion.models import Message
Member9 = Member.objects.get(id=10)
m = Message(message_text='Bonjour',pub_date=timezone.now(),views=9,member=Member9)
#Pour repondre a un message avec un ou plusieurs users d'un groupe
Member7 = Member.objects.get(id=8)
sujet = Message.objects.get(id=1)
response3=Message(message_text='Merci Bonjour,Tres bien',pub_date=timezone.now(),views=4,sujet=sujet,member=Member7)

#Pour compter le nombres de messages
Message.objects.count()

#Pour creer une classe MemberShip
from Discussion.models import MemberShip
Group1 = Group.objects.get(id=1)
Ms = MemberShip(group=Group1, member= Member7, is_creator ='True')

#Pour avoir les 10 derniers messages qui ont ete publier:
latest_messages = Message.objects.order_by('-pub_date') [:10]
print(latest_messages)

Message.objects.filter(pub_date__isnull=True)


#Pour recuperer les messages d'un groupe preci
group1=Group.objects.get(id=1)
Message.objects.filter(groupe=group1)

#lister les membres d'un groupe
groups = Group.objects.get(id=1)
groups_member = groups.members.all()
# groupmember_list = Member.objects.exclude(group__id=pk)
# for x in groupmember_list:
#     print(x)