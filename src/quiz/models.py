from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class MyUserManager(BaseUserManager):
    
    def create_user(self, matricule, prenom, nom, codeSecteur, password=None):
        if not prenom:
            raise ValueError("Prenom requis")
        if not nom:
            raise ValueError("nom requis")
        if not matricule:
            raise ValueError("matricule requis")
        if not codeSecteur:
            raise ValueError("codeSecteur requis")
        
        secteur, __ = Secteur.objects.get_or_create(
            codeSecteur=codeSecteur, defaults={'nomSecteur': codeSecteur}
        )
        
        user=self.model(
            prenom = prenom,
            nom = nom,
            matricule = matricule,
            codeSecteur = secteur
        )
        user.set_password(password)
        user.save()
        # user.save(using=self._db)
        return user
    
    def create_superuser(self, prenom, nom, matricule, codeSecteur, password=None):
        user=self.create_user(
            prenom = prenom,
            nom = nom,
            matricule = matricule,
            codeSecteur = codeSecteur,
            password = password            
        )
        
        user.is_admin=True
        user.is_superuser=True
        # user.save(using=self._db)
        user.save()
        return user

class Secteur(models.Model):
    nomSecteur = models.CharField(verbose_name = "nomSecteur", max_length=50)
    codeSecteur = models.CharField(verbose_name = "codeSecteur", max_length=3, primary_key=True)
    
    class Meta:
        db_table = "Secteur"
    
class Personnel(AbstractBaseUser): #models.Model #AbstractBaseUser
    prenom = models.CharField(verbose_name = "prenom", max_length=20)
    nom = models.CharField(verbose_name = "nom", max_length=20)
    matricule = models.CharField(verbose_name="matricule", max_length=20, primary_key=True)
    codeSecteur = models.ForeignKey(Secteur, on_delete=models.CASCADE)
    
    USERNAME_FIELD="matricule"
    REQUIRED_FIELDS = ["nom", "prenom", "codeSecteur"]
    
    objects = MyUserManager()
    
    class Meta:
        db_table = "Personnel"


class Collaborateur(models.Model):
    matricule = models.OneToOneField('Personnel', models.DO_NOTHING, db_column='matricule', primary_key=True)

    class Meta: db_table = 'Collaborateur'

class Superuser(models.Model):
    matricule = models.OneToOneField(Personnel, models.DO_NOTHING, db_column='matricule', primary_key=True)
    role = models.BooleanField()

    class Meta: db_table = 'Superuser'