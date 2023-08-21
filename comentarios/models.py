from django.db import models

# AQUÍ CREAM LO QUE SERIEN SES TAULES DE SA BBDD
class Comment(models.Model):
    # OJO SI NO POSAM SI POT SER NULL O NO, I NO TÉ VALOR PER DEFECTE
    name = models.CharField(max_length=250, null=False)
    score = models.IntegerField(default=3)
    comment = models.TextField(max_length=1000, null=True)
    date = models.DateField(null=True)

    # SI CONSULTAMOS EL OBJETO QUE NOS DEVUELVA LA INFO CON EL FORMATO QUE QUEREMOS
    def __str__(self) -> str:
        return self.name