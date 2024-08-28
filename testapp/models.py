from django.db import models

class ModelTest(models.Model):
    mon_champ = models.CharField(max_length=128)

    def toto(self):
        return "mc2i"

    def __str__(self):
        return self.mon_champ
    
    def get_absolute_url(self):
        return ""


class ModelToto(models.Model):
    mon_champ = models.CharField(max_length=128)