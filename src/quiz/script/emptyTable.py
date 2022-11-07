from quiz.models import Personnel, Collaborateur, Superuser
Collaborateur.objects.all().delete()
Superuser.objects.all().delete()
Personnel.objects.all().delete()