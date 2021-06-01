from django.urls import path

from libros import views

urlpatterns = [
    path('libros-comprados', views.libros_comprados, name='LibrosComprados'),
    path('libros-usados', views.libros_usados, name='LibrosUsados'),
    path('total-libros', views.reporte_total_libros, name='TotalLibros'),
]
