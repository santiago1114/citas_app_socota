from django.shortcuts import redirect, get_object_or_404, render
from .models import Turno, Paciente
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Media

def index(request):
    media_items = Media.objects.all()
    return render(request, 'turnos.html', {'media_items': media_items})


def carousel_view(request):
    media_items = Media.objects.all()
    return render(request, 'carousel_template.html', {'media_items': media_items})


def crear_turno(request, id):
    # Retrieve the instance of Paciente using the id
    instance = get_object_or_404(Paciente, id=id)
    
    # Save the instance
    instance.save()
    
    # Crea el turno
    instance.turno_set.create()
    
    # Redirect to a refresh
    return redirect('/admin/appointments/turno/')


def cerrar_turno(request, id):
    # Retrieve the instance of Turno using the id
    instance = get_object_or_404(Turno, id=id)
    
    # Change the value of the field
    instance.en_espera = False
    
    # Save the instance
    instance.save()
    
    # Enviar evento socket
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'turno_group',  # Group name
        {
            'type': 'send_turno',
            'instance': instance,
        }
    )
     
    # Redirect to a refresh
    return redirect(request.META.get('HTTP_REFERER'))



def llamar_turno(request, id):
    # Retrieve the instance of Turno using the id
    instance = get_object_or_404(Turno, id=id)
    
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'turno_group',  # Group name
        {
            'type': 'send_turno',
            'instance': instance,
        }
    )
    
    # Redirect to a refresh
    return redirect(request.META.get('HTTP_REFERER'))