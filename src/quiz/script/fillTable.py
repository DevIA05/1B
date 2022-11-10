###################################################
########## À partir du shell python ###############
###################################################
from . import models
from quiz.models import Personnel, Collaborateur, Superuser, Secteur
import names
from random import randint

s1 = Secteur.objects.create(nomsecteur="marketing", codesecteur="MKT"); s1.save()
s2 = Secteur.objects.create(nomsecteur="informatique", codesecteur="INF"); s2.save()
for i in range(20):
    n = names.get_full_name().split(" ")
    p = Personnel.objects.create_user(prenom=n[0], nom=n[1], matricule=str(i).zfill(2), codesecteur="TTT", password=str(i).zfill(2))
    p.save()
    if i < 10:
           c = Collaborateur.objects.create(matricule=Personnel.objects.get(pk=str(i).zfill(2))); c.save()
    else:
            su = Superuser.objects.create(matricule=Personnel.objects.get(pk=str(i).zfill(2)), role=randint(0,1)); su.save()

###################################################
############## À partir de python #################
###################################################

# Les fichiers .json générés sont stockés dans le dossier quiz/data
# et les données doivent être ajouté avec python manage.py loaddata 

# from random import randint, randrange
# import time
# import names
# from datetime import timedelta
# from datetime import datetime


# def random_date(start, end):
#     """
#     This function will return a random datetime between two datetime
#     objects.
#     """
#     delta = end - start
#     int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
#     random_second = randrange(int_delta)
#     return start + timedelta(seconds=random_second)

# def personne():
#     f = open("quiz/data/personne.json", "a")
#     f.write("[")
#     for i in range(1,21):
#         n = names.get_full_name().split(" ")
#         f.write(str({
#             "pk": str(i).zfill(2),
#             "model": "quiz.Personnel",
#             "fields": {
#                 "password": str(i).zfill(2),
#                 "prenom": n[0],
#                 "nom": n[1],
#                 "codesecteur": "TTT"}
#             })+str(",\n"))
#     f.write("]")
#     f.close()
    
# def collab():
#     f = open("quiz/data/collab.json", "a")
#     f.write("[")
#     for i in range(1,11):
#         f.write(str({
#             "pk": str(i).zfill(2),
#             "model": "quiz.Collaborateur",
#             "fields": { }
#             })+str(",\n"))
#     f.write("]")
#     f.close()
    
# def superuser():
#     f = open("quiz/data/superuser.json", "a")
#     f.write("[")
#     for i in range(11,21):
#         f.write(str({
#             "pk": str(i).zfill(2),
#             "model": "quiz.Superuser",
#             "fields": {
#                 "role": randint(0,1)
#             }
#             })+str(",\n"))
#     f.write("]")
#     f.close()

# import os
# print(os.getcwd())
#personne()
#collab()
#superuser()