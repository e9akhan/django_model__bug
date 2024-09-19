from django.db import models

# Create your models here.
class ABCModel(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True


class ConcreteModel(ABCModel):
    description = models.TextField()