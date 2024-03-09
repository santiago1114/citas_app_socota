from django.db import models
from django.utils import timezone


class Paciente(models.Model):
    TIPO_DOCUMENTO = (
        ("CC", "Cédula de ciudadanía"),
        ("CE", "Cédula de extranjería"),
        ("DE", "Documento extranjero"),
        ("NIT", "NIT"),
        ("PA", "Pasaporte"),
    )
    nombres = models.CharField(max_length=64)
    apellidos = models.CharField(max_length=64)
    tipo_documento = models.CharField(max_length=16,
                                      choices=TIPO_DOCUMENTO,
                                      default="CC",
                                      help_text="Seleccionar el tipo de documento")
    numero_documento = models.CharField(max_length=16, null=True)
    celular = models.CharField(max_length=16, null=True, blank=True)
    fecha_de_registro = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f"{self.numero_documento}: {self.nombres} {self.apellidos}"
    

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    confirmado = models.BooleanField(default=False)
    asistio = models.BooleanField(default=False, help_text='Esta casilla se marca automaticamente cuando se genera un turno y se cierra')
    
    def __str__(self):
        return f"{self.paciente.numero_documento}: {self.paciente.nombres} {self.paciente.apellidos}"


class Turno(models.Model):
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    en_espera = models.BooleanField(default=True)
    fecha_de_apertura = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f"Turno de {self.cita} - {self.en_espera}"
    
    
class Media(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='carousel/')
    is_video = models.BooleanField(default=False, verbose_name="Es un video", help_text='Seleccione cuando cargue un video (debe ser formato mp4)')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Imágen o Video"  # Set the custom verbose name for your model
        verbose_name_plural = "Imagenes o Videos"  # Option
