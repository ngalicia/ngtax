from django.db import models

# Create your models here.

class LibroComprado(models.Model):
    fecha_adquisicion=models.DateField()
    cantidad_venta=models.IntegerField()
    cantidad_compra=models.IntegerField()

    def __str__(self):
        return 'Fecha: %s - Compra: %s - Venta: %s' %(self.fecha_adquisicion, self.cantidad_compra, self.cantidad_venta)


class LibroUsado(models.Model):
    periodo=models.IntegerField()
    cantidad_venta=models.IntegerField()
    cantidad_compra=models.IntegerField()

    def __str__(self):
        return 'Periodo: %s - Compra: %s - Venta: %s' %(self.periodo, self.cantidad_compra, self.cantidad_venta)
