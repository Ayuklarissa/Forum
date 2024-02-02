from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Group (models.Model):
    id = models.IntegerField(primary_key= True)
    name = models.CharField(max_length=50, default="anonymous")
    topic= models.CharField(max_length=300)
    description = models.CharField(max_length=200,blank=True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    def __str__(self):
        return str (self.topic)

class Member(models.Model):
    id = models.IntegerField(primary_key= True)
    name = models.CharField(max_length=50)
    e_mail = models.CharField(max_length=50,null=True)
    role = models.CharField(max_length=20)
    date_inscription = models.DateTimeField(auto_now_add = True, null = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    groups = models.ManyToManyField(
        Group,
        through="MemberShip",
        through_fields=("member", "group"),
    )
    def __str__(self):
        return str (self.role)

class Message(models.Model):
    id = models.IntegerField(primary_key= True)
    message_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    views = models.IntegerField(default=0)
    sujet = models.ForeignKey("self", on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.message_text)
    
class MemberShip(models.Model):
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    member = models.ForeignKey('Member',on_delete=models.CASCADE)
    is_creator = models.BooleanField(default=True)
    