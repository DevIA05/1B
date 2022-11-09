###################################################
########## À partir du shell python ###############
###################################################

import names
from quiz.models import Personnel, Collaborateur, Superuser, Secteur
import names
from random import randint

s1 = Secteur.objects.create(nomsecteur="marketing", codesecteur="MKT"); s1.save()
s2 = Secteur.objects.create(nomsecteur="informatique", codesecteur="INF"); s2.save()
for i in range(20):
       n = names.get_full_name().split(" ")
       p = Personnel.objects.create_user(prenom=n[0], nom=n[1], matricule=str(i).zfill(2), codesecteur="MKT", password=str(i).zfill(2))
       p.save()
       if i < 10:
              c = Collaborateur.objects.create(matricule=Personnel.objects.get(pk=str(i).zfill(2))); c.save()
       else:
              su = Superuser.objects.create(matricule=Personnel.objects.get(pk=str(i).zfill(2)), role=randint(0,1)); su.save()
