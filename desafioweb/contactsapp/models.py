from django.db import models

# Create your models here.
class Contact( models.Model ):
    CHANNELS = (
        ('Tel', 'Telefone'),
        ('Email', 'Email'),
        ('Cel', 'Celular')
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    channel = models.CharField(max_length=5, choices=CHANNELS)
    value = models.CharField(max_length=60)
    description = models.TextField(default='none')

    def __str__(self):
        return self.name