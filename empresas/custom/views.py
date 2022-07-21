from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from custom.forms import formaCliente

# Create your views here.
from custom.models import Cliente


def bienvenidos(request):
    return render(request, 'welcome/bienvenidos.html')


def cstm(request):
    cliente = Cliente.objects.order_by('id_cliente')
    busqueda = request.GET.get('buscar')

    if busqueda:
        cliente = Cliente.objects.filter(
        Q(id_cliente__icontains = busqueda) |
        Q(apellidopaterno__icontains = busqueda) |
        Q(apellidomaterno__icontains = busqueda) |
        Q(nombre__icontains = busqueda)
        ).distinct()

    return render(request,'welcome/clientes.html',{'cliente':cliente})


def detalle_custom(request, id):
    detalle = get_object_or_404(Cliente,pk=id)
    return render(request,'welcome/detalle_cliente.html',{'detalle':detalle})


def nuevo_cliente(request):
    if request.method == 'POST':
        formCliente = formaCliente(request.POST)
        if formCliente.is_valid():
            formCliente.save()
            return redirect('index')
        else:
            return render(request, 'welcome/nuevo_cliente.html',{'formCliente':formCliente})
    else:
        formCliente = formaCliente()
        return render(request, 'welcome/nuevo_cliente.html', {'formCliente': formCliente})


def editar_custom(request, id):
    cliente = get_object_or_404(Cliente,pk=id)
    if request.method == 'POST':
        formCliente = formaCliente(request.POST, instance=cliente)
        if formCliente.is_valid():
            formCliente.save()
            return redirect('customers')
        else:
            return render(request,'welcome/editarCustom.html',{'formCliente':formCliente})
    else:
        formCliente  = formaCliente(instance=cliente)
        return render(request,'welcome/editarCustom.html',{'formCliente':formCliente})


def elimar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    if cliente:
        cliente.delete()
    return redirect('customers')