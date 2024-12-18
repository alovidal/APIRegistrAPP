from django.db import models

class SedeInstitucion(models.Model):
    nombre = models.CharField(max_length=100, primary_key=True, db_column="nombre")
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return f"Sede {self.nombre}"
    
class Asignatura(models.Model):
    nombreAsignatura = models.CharField(max_length=100, primary_key=True, db_column="nombreAsignatura")
    codigo = models.CharField(max_length=100)
    seccion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombreAsignatura} - {self.codigo}_{self.seccion}"

class Usuario(models.Model):
    username = models.CharField(max_length=100, primary_key=True, db_column="username")
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    sede = models.ForeignKey(SedeInstitucion, on_delete=models.CASCADE, db_column="nombre") 
    asignaturas = models.ManyToManyField(Asignatura,related_name="usuarios" , db_column="nombreAsignatura")

    def __str__(self):
        return f"{self.username} - {self.sede.nombre}"

class Asistencia(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column="username")
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, db_column="nombreAsignatura")
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    presente = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usuario.username} - {self.asignatura.nombreAsignatura} - {self.presente}"
