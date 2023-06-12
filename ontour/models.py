from django.db import models

# Create your models here.

class Pagos (models.Model):
    id_pago             = models.AutoField(primary_key= True, max_length = 10, db_column ='IdPago')
    cantidad_pago       = models.IntegerField(blank = False, null = False)
    fecha_pago          = models.DateField(blank = False, null = False)
    id_tipo_pago        = models.ForeignKey("Tipo_pago", on_delete=models.CASCADE, blank = False, null = False, max_length=50)
    id_curso            = models.ForeignKey("curso", on_delete=models.CASCADE)

    def __str__(self):
        return ("Deposito con id")+ " " + str(self.id_pago)
    
class Tipo_pago(models.Model):
    id_tipo_pago = models.AutoField(primary_key=True, max_length=10, db_column='IdTipoPago')
    Tipo_pago = models.CharField(blank=False, null=False, max_length=50)

    def __str__(self):
        return str(self.Tipo_pago)

 
class paquete_turistico (models.Model):
    id_paquete          = models.AutoField(primary_key = True, db_column='PaqueteTuristico')
    nombre_paquete      = models.CharField(blank = False, null = False, max_length=50)

    def __str__(self):
        return str(self.nombre_paquete)

class colegio (models.Model):
    id_colegio          = models.AutoField(primary_key = True)
    nombre_colegio      = models.CharField(blank = False, null = False, max_length=50)
    
    def __str__(self):
        return str(self.nombre_colegio)

class curso (models.Model):
    id_curso            = models.AutoField(primary_key = True, db_column= 'IdCurso')
    nivel_curso         = models.CharField(blank = False, null = False, max_length= 15)
    seccion_curso       = models.CharField(blank = False, null = False, max_length= 1)
    id_colegio          = models.ForeignKey("colegio", on_delete=models.CASCADE)
    id_cuenta_viaje     = models.ForeignKey("estado_pago",blank = False, null = False, on_delete=models.CASCADE)

    def __str__(self):
        return str (self.id_colegio)+ " "  +(self.nivel_curso)+ " " +(self.seccion_curso)

class estado_pago (models.Model):
    id_cuenta_viaje     = models.AutoField(primary_key= True, max_length = 10, db_column ='IdCuenta')
    cantidad_actual     = models.IntegerField(max_length = 10,blank = False, null = False)
    cantidad_total      = models.IntegerField(max_length = 10,blank = False, null = False)
    id_pago             = models.ForeignKey("Pagos", on_delete=models.CASCADE)

    def __str__(self):
        return ("Numero de cuenta")+ " " +str(self.id_cuenta_viaje)

class Alumno(models.Model):
    rut_alumno          = models.CharField(primary_key=True, max_length=10)
    nombre_alumno       = models.CharField(blank = False, null = False, max_length=20)
    appaterno_alumno    = models.CharField(blank = False, null = False, max_length=20)
    apmaterno_alumno    = models.CharField(blank = False, null = False, max_length=20)
    edad                = models.IntegerField(blank = False, null = False, max_length = 3) 
    id_genero           = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero') 
    alergias            = models.CharField(blank = False, max_length=50) 
    id_curso            = models.ForeignKey("curso", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre_alumno)+" "+str(self.appaterno_alumno)+ " "+ str(self.apmaterno_alumno) 

class Genero(models.Model):
    id_genero  = models.AutoField(db_column='idGenero', primary_key=True) 
    genero     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)
 
class Apoderado (models.Model):
    rut_apoderado           = models.CharField(primary_key = True, max_length=10)
    nombre_apoderado        = models.CharField(blank = False, null = False, max_length=50)
    appaterno_alumno        = models.CharField(blank = False, null = False, max_length=20)
    apmaterno_alumno        = models.CharField(blank = False, null = False, max_length=20)
    edad                    = models.IntegerField(blank = False, null = False, max_length = 3) 
    telefono                = models.IntegerField(blank = False, null = False, max_length = 9)
    email                   = models.EmailField(blank = False, null = False, max_length=254)
    id_genero               = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')
    rut_alumno              = models.ForeignKey("Alumno", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre_apoderado)+" "+str(self.appaterno_alumno)+ " "+ str(self.apmaterno_alumno) 

class contrato (models.Model):
    id_contrato             = models.AutoField(primary_key = True, max_length = 8)
    fecha_contrato          = models.DateField(blank = False, null = False)
    fecha_evento            = models.DateField(blank = False, null = False)
    fecha_de_pago           = models.DateField(blank = False, null = False)
    monto_reserva           = models.IntegerField(blank = False, null = False)
    id_paquete              = models.ForeignKey("paquete_turistico", on_delete=models.CASCADE, blank = False, null = False, max_length=50)
    id_cuenta_viaje         = models.ForeignKey("estado_pago", on_delete=models.CASCADE)
    rut_apoderado           = models.ForeignKey("Apoderado", on_delete=models.CASCADE)
    id_curso                = models.ForeignKey("curso", on_delete=models.CASCADE)


    def __str__(self):
        return ("Contrato de")+ " " + str(self.id_curso)    
