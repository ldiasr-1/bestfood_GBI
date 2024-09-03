from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if self.nome:
            self.first_name = self.nome
        if self.sobrenome:
            self.last_name = self.sobrenome
        super(CustomUser, self).save(*args, **kwargs)