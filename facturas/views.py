from django.shortcuts import render
from django.contrib import messages
from facturas.models import Factura, Proveedor, Documento
from django.db.models import Count
from django.db.models import Sum

# Create your views here.

def facturas(request):
    
    periodos=Factura.objects.values('periodo').filter(estado='1').annotate(periodo_count=Count('periodo'))

    if request.method == 'POST':
        prd=int(request.POST['prd'])
        tipo=int(request.POST['tipo'])
        facturas=Factura.objects.filter(periodo=prd, tipo=tipo, estado='1')
        return render(request, "facturas/facturas.html", {'facturas': facturas, 'periodos': periodos, 'prd_actual': prd, 'tip_actual': tipo})

    return render(request, "facturas/facturas.html", {'periodos': periodos})


def nueva_factura(request):

    proveedores=Proveedor.objects.values('proveedor', 'nombre').order_by('proveedor')
    documentos=Documento.objects.values('id', 'nombre').order_by('id')

    if request.method == 'POST':
        periodo=request.POST['periodo']
        fecha=request.POST['fecha']
        proveedor=request.POST['proveedor']
        documento=request.POST['documento']
        serie=request.POST['serie']
        numero=request.POST['numero']
        total=request.POST['total']
        exento=request.POST['exento']
        tipo=request.POST['tipo']
        estado=request.POST['estado']

        pro=Proveedor.objects.get(proveedor=proveedor)
        doc=Documento.objects.get(id=documento)

        f = Factura(periodo=periodo, proveedor=pro, documento=doc, serie=serie, numero=numero, fecha=fecha, total=total, total_exento=exento, tipo=tipo, estado=estado)
        f.save()
        
        messages.success(request, 'Factura %s - %s creada exitosamente.' %(serie, numero))
        #messages.error(request, 'Error al crear factura %s - %s.' %(serie, numero))

    return render(request, "facturas/nueva_factura.html", {'proveedores': proveedores, 'documentos': documentos})


def editar_factura(request, id):

    proveedores=Proveedor.objects.values('proveedor', 'nombre').order_by('proveedor')
    documentos=Documento.objects.values('id', 'nombre').order_by('id')
    factura=Factura.objects.get(id=id)

    if request.method == 'POST':
        periodo=request.POST['periodo']
        fecha=request.POST['fecha']
        proveedor=request.POST['proveedor']
        documento=request.POST['documento']
        serie=request.POST['serie']
        numero=request.POST['numero']
        total=request.POST['total']
        exento=request.POST['exento']
        tipo=request.POST['tipo']
        estado=request.POST['estado']

        pro=Proveedor.objects.get(proveedor=proveedor)
        doc=Documento.objects.get(id=documento)

        factura.periodo=periodo
        factura.proveedor=pro
        factura.documento=doc
        factura.serie=serie
        factura.numero=numero
        factura.fecha=fecha
        factura.total=total
        factura.total_exento=exento
        factura.tipo=tipo
        factura.estado=estado

        factura.save()
        
        messages.success(request, 'Factura %s - %s editada exitosamente.' %(serie, numero))
        #messages.error(request, 'Error al editar factura %s - %s.' %(serie, numero))

    return render(request, "facturas/editar_factura.html", {'proveedores': proveedores, 'documentos': documentos, 'factura': factura})


def eliminar_factura(request, id):
    
    factura=Factura.objects.get(id=id)
    factura.delete()

    messages.success(request, 'Factura %s - %s eliminada exitosamente.' %(factura.serie, factura.numero))
    #messages.error(request, 'Error al eliminar factura %s - %s.' %(factura.serie, factura.numero))

    periodos=Factura.objects.values('periodo').filter(estado='1').annotate(periodo_count=Count('periodo'))

    return render(request, "facturas/facturas.html", {'periodos': periodos})


def reporte_credito_fiscal(request):
    
    periodos=Factura.objects.values('periodo').filter(estado='1').annotate(periodo_count=Count('periodo'))

    if request.method == 'POST':
        prd=int(request.POST['prd'])
        facturas_total_ventas=Factura.objects.filter(periodo=prd, tipo='2', estado='1').aggregate(facturas_total=Sum('total'))
        facturas_credito_ventas=Factura.objects.filter(periodo=prd, tipo='2', estado='1').aggregate(credito_fiscal=Sum('total')/1.12*0.12)
        facturas_total_compras=Factura.objects.filter(periodo=prd, tipo='1', estado='1').aggregate(facturas_total=Sum('total'))
        facturas_credito_compras=Factura.objects.filter(periodo=prd, tipo='1', estado='1').aggregate(credito_fiscal=Sum('total')/1.12*0.12)
        return render(request, "facturas/reporte_credito_fiscal.html", {'facturas_total_ventas': facturas_total_ventas, 'facturas_credito_ventas': facturas_credito_ventas,'facturas_total_compras': facturas_total_compras, 'facturas_credito_compras': facturas_credito_compras, 'periodos': periodos, 'prd_actual': prd})

    return render(request, "facturas/reporte_credito_fiscal.html", {'periodos': periodos})


def reporte_cantidad_facturas(request):
    
    periodos=Factura.objects.values('periodo').filter(estado='1').annotate(periodo_count=Count('periodo'))

    if request.method == 'POST':
        prd=int(request.POST['prd'])
        facturas=Factura.objects.filter(periodo=prd, tipo='1', estado='1').count()
        proveedores=Factura.objects.values('proveedor').filter(periodo=prd, tipo='1', estado='1').distinct().count()
        return render(request, "facturas/reporte_cantidad_facturas.html", {'facturas': facturas, 'proveedores': proveedores, 'periodos': periodos, 'prd_actual': prd})

    return render(request, "facturas/reporte_cantidad_facturas.html", {'periodos': periodos})
