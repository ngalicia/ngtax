from django.shortcuts import render
from libros.models import LibroComprado, LibroUsado
from django.db.models import Sum

# Create your views here.

def libros_comprados(request):

    libros=LibroComprado.objects.all()
    return render(request, "libros/libros_comprados.html", {'libros': libros})


def libros_usados(request):

    libros=LibroUsado.objects.all()
    return render(request, "libros/libros_usados.html", {'libros': libros})


def reporte_total_libros(request):
    
    libros_comprados_compra=LibroComprado.objects.aggregate(total_compra=Sum('cantidad_compra'))
    libros_comprados_venta=LibroComprado.objects.aggregate(total_venta=Sum('cantidad_venta'))
    libros_usados_compra=LibroUsado.objects.aggregate(total_compra=Sum('cantidad_compra'))
    libros_usados_venta=LibroUsado.objects.aggregate(total_venta=Sum('cantidad_venta'))
    resto_libros_compra=libros_comprados_compra['total_compra']-libros_usados_compra['total_compra']
    resto_libros_venta=libros_comprados_venta['total_venta']-libros_usados_venta['total_venta']
    return render(request, "libros/reporte_total_libros.html", {'resto_libros_compra': resto_libros_compra, 'resto_libros_venta': resto_libros_venta})
