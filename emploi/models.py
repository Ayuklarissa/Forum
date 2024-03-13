from django.db import models
from django.contrib.auth.models import User

# Create your models here.


    

class OffreEmploi(models.Model):
    id = models.AutoField(primary_key= True)
    entreprise_name = models.CharField(max_length=100)
    poste = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description_entreprise = models.TextField()
    mission = models.TextField()
    require_profil = models.TextField()
    pub_date = models.DateTimeField(auto_now_add = True, null = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return str(self.poste)
    

class Candidature(models.Model):
    id = models.AutoField(primary_key= True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100,null=True)
    e_mail = models.EmailField(max_length=50,null=True)
    cv = models.FileField(upload_to='candidatures/')
    lettre_motivation = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, null = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    offre_emploi = models.ForeignKey(OffreEmploi, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nom)