from django.db import models
from django.contrib.auth.models import User, Permission
# Create your models here.

class Member(models.Model):
    id = models.IntegerField(primary_key= True)
    name = models.CharField(max_length=50)
    e_mail = models.CharField(max_length=50,null=True)
    role = models.CharField(max_length=20)
    date_inscription = models.DateTimeField(auto_now_add = True, null = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str (self.name)
class Group (models.Model):
    id = models.IntegerField(primary_key= True)
    name = models.CharField(max_length=50, default="anonymous")
    topic= models.CharField(max_length=300)
    description = models.CharField(max_length=200,blank=True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    members = models.ManyToManyField(
        Member,
        through="MemberShip",
        through_fields=( "group","member")
    )
    def __str__(self):
        return str (self.name)

class Message(models.Model):
    id = models.IntegerField(primary_key= True)
    message_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    views = models.IntegerField(default=0)
    sujet = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    groupe = models.ForeignKey(Group, on_delete=models.CASCADE,default=1)
    def __str__(self):
        return str(self.message_text)
    
class MemberShip(models.Model):
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    member = models.ForeignKey('Member',on_delete=models.CASCADE)
    is_creator = models.BooleanField(default=True)
    def __str__(self):
        return str(self.member)
    