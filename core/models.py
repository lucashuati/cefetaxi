from django.db import models
from django.conf import settings

class Motorista(models.Model):
    django_user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def whoamI(self):
        return "Motorista"

class Associado(models.Model):
    django_user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def whoamI(self):
        return "Associado"
