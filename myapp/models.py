from django.db import models

class ModelTest(models.Model):
    mon_champ = models.CharField(max_length=128)

class ModelToto(models.Model):
    mon_champ = models.CharField(max_length=128)