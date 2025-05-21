from django.db import models
from django_mongodb_backend.fields import EmbeddedModelField, ArrayField
from django_mongodb_backend.models import EmbeddedModel

class Termo(models.Model):
    termo = models.CharField(max_length=200)
    traducao = models.CharField(max_length=200)
    descricao = models.CharField(max_length=500)
    codigo = models.CharField(max_length=200)

    class Meta:
        db_table = "dict_termos"
        managed = False

    
    def __str__(self):
        return self.termo