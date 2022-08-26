from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    ism = models.CharField(max_length=50)
    email = models.EmailField()
    tel = models.CharField(max_length=13)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism

class Vedio(models.Model):
    nom = models.CharField(max_length=100)
    vedio = models.FileField()
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.nom



class Pleylist(models.Model):
    nom = models.CharField(max_length=100)
    vediolar = models.ManyToManyField(Vedio)
    ochiq = models.BooleanField(default=True)
    def __str__(self):
        return self.nom


class Obuna(models.Model):
    obunalar = models.OneToOneField(Account, on_delete=models.SET_NULL, null=True, related_name="obunalar")
    obunachilar = models.OneToOneField(Account, on_delete=models.SET_NULL, null=True, related_name="obunachilar")


class Like(models.Model):
    video = models.OneToOneField(Vedio, on_delete=models.SET_NULL, null=True)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)

class History(models.Model):
    nom = models.CharField(max_length=100)
    vedio = models.FileField()
    account = models.OneToOneField(Account, on_delete=models.SET_NULL, null=True)