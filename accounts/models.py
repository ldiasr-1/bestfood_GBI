from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='accounts_customuser_set', 
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='accounts_customuser_set',  
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def save(self, *args, **kwargs):
        self.first_name = self.nome
        self.last_name = self.sobrenome
        super().save(*args, **kwargs)