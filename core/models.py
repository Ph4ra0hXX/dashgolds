from django.db import models


class Menu(models.Model):
    nome = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    url = models.CharField(max_length=100, unique=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"
