from django.urls import path

from facturas import views

urlpatterns = [
    path('facturas', views.facturas, name='Facturas'),
    path('nueva-factura', views.nueva_factura, name='NuevaFactura'),
    path('editar-factura/<int:id>', views.editar_factura, name='EditarFactura'),
    path('eliminar-factura/<int:id>', views.eliminar_factura, name='EliminarFactura'),
    path('credito-fiscal', views.reporte_credito_fiscal, name='CreditoFiscal'),
    path('cantidad-facturas', views.reporte_cantidad_facturas, name='CantidadFacturas'),
]
