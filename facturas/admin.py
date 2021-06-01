from django.contrib import admin
from facturas.models import Factura, Proveedor, Documento

# Register your models here.

class FacturaAdmin(admin.ModelAdmin):
	list_display=("periodo", "proveedor", "documento", "serie", "numero", "fecha", "total", "total_exento", "tipo", "estado")
	search_fields=("serie", "numero")
	list_filter=['periodo']


admin.site.register(Factura, FacturaAdmin)
admin.site.register(Proveedor)
admin.site.register(Documento)
