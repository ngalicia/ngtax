from django.db import models
from datetime import datetime

# Create your models here.

class Proveedor(models.Model):
	proveedor=models.CharField(primary_key = True, max_length=15)
	nombre=models.CharField(max_length=100)

	def __str__(self):
		return '%s - %s' %(self.proveedor, self.nombre)

	def get_id(self):
		return self.proveedor


class Documento(models.Model):
	nombre=models.CharField(max_length=100)

	def __str__(self):
		return '%s - %s' %(self.id, self.nombre)

	def get_id(self):
		return self.id


class Factura(models.Model):
	periodo=models.IntegerField()
	proveedor=models.ForeignKey(Proveedor, on_delete=models.CASCADE)
	documento=models.ForeignKey(Documento, on_delete=models.CASCADE)
	serie=models.CharField(max_length=15)
	numero=models.CharField(max_length=15)
	fecha=models.DateField()
	total=models.FloatField() # Total grabado
	total_exento=models.FloatField() # Total exento
	tipo=models.IntegerField() # 1:Compra, 2:Venta
	estado=models.IntegerField() # 1:Activo, 2:Eliminado
	
	def get_fecha(self):
		if isinstance(self.fecha, str):
			date_time_obj = datetime.strptime(self.fecha, '%Y-%m-%d')
			return date_time_obj.strftime("%Y-%m-%d")

		return self.fecha.strftime("%Y-%m-%d")
