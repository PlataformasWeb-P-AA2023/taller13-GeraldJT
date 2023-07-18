from django.db import models

# Create your models here.

class Edificio(models.Model):
    opciones_tipo_Edificio = (
        ('residencial', 'Residencial'),
        ('comercial', 'Comercial'),
    )
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30, unique=True)
    tipo = models.CharField(max_length=30,\
                            choices= opciones_tipo_Edificio)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.direccion,
                self.ciudad,
                self.tipo)

class Propietario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.IntegerField()
    def __str__(self):
        return "%s %s %s" % (self.nombre,
                self.apellido,
                self.cedula)

    def get_departamentos(self):
        departamento = self.departamentos.all()
        return len(departamento)
    
    def get_edificios(self):
        departamento = self.departamentos.all()
        nombre_edificio = []
        for d in departamento:
            nombre_edificio.append(d.edificio.nombre)
        return set(nombre_edificio) 
        
 
          
class Departamento(models.Model):
    costo = models.IntegerField()
    numero_cuartos = models.IntegerField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="numero_departamentos")
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE,
            related_name="departamentos")
    def __str__(self):
        return "%s %s %s %s" % (self.costo,
                self.numero_cuartos,
                self.edificio,
                self.propietario)
