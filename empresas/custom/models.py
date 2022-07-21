from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellidopaterno = models.CharField(max_length=45)
    apellidomaterno = models.CharField(max_length=45)
    telefono = models.IntegerField()
    ciudad = models.CharField(max_length=45)
    estado = models.CharField(max_length=45)
    totaldeuda = models.DecimalField(max_digits=8,decimal_places=2)
    tipos = (('A','Mayor'),('B','Medio'),('C','Bajo'))
    tipocliente = models.CharField(max_length=1, choices=tipos)

    def __str__(self):
        return f'{self.id_cliente}{self.nombre}{self.apellidopaterno}{self.apellidomaterno}{self.telefono}{self.ciudad}{self.estado}{self.totaldeuda}{self.tipocliente}'
