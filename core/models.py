from django.db import models

class Entidade(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)

    def __str__(self):
        return self.nome

