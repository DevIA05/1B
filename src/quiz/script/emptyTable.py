from quiz.models import Personnel, Collaborateur, Superuser, Secteur
Collaborateur.objects.all().delete()
Superuser.objects.all().delete()
Personnel.objects.all().delete()
Secteur.objects.all().delete()