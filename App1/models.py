from django.db import models

# Create your models here.
class ProyectoDb(models.Model):
    nombreP = models.CharField(max_length=100,verbose_name="Nombre")
    descripcionP = models.TextField(verbose_name='Descripcion',max_length=400,default='')
    fechaI = models.DateField(verbose_name='Fecha Creacion',null=False,blank=False)
    fechaF = models.DateField(verbose_name='Fecha Fin',null=True,blank=True)    
    responsable = models.CharField(max_length=50,verbose_name='Responsable',null=False)
    estado = models.BooleanField(default=False)   

    class Meta:
        db_table="Proyectos"
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.nombreP
class UsuarioDb(models.Model):
    nombreU = models.CharField(max_length=50,verbose_name="Nombre")
    email = models.EmailField(max_length=30,verbose_name="Email")
    telefono=models.CharField(max_length=10,verbose_name='Telefono')    

    class Meta:
        db_table="Usuarios"
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
    def __str__(self):
        return self.nombreU
class TareaDb(models.Model):
    nombreT = models.CharField(max_length=100,verbose_name="Nombre")
    fecha_inicio = models.DateField(verbose_name='Fecha Inicia')
    fecha_fin = models.DateField(verbose_name='Fecha Fin')
    asignado = models.ForeignKey(UsuarioDb, on_delete=models.CASCADE,verbose_name="Responsables")
    proyecto_fk = models.ForeignKey(ProyectoDb, on_delete=models.CASCADE,verbose_name='Proyecto') 
    done = models.BooleanField(default=False)

    class Meta:
        db_table="Tareas"
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"

    def __str__(self):
        return self.nombreT




    


    