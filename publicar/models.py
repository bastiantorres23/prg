from django.db import models




gen=[{"Masculino","Masculino."},
    {"Femenino","Femenino."}]



class Estacion(models.Model):
    NombreE=models.CharField(verbose_name="Nombre Estacion", max_length=15)
    class Meta:
        verbose_name="Estacion"
        verbose_name_plural="Estaciones"

    def __str__(self):
        return self.NombreE
    




class Categoria(models.Model):
    Nombrec=models.CharField(verbose_name="Nombre Categoria", max_length=30)
    estacionc=models.ForeignKey(Estacion,null=True,on_delete=models.SET_NULL)
    crea=models.DateTimeField(auto_now_add=True)
    upda=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"

    def __str__(self):
        return self.Nombrec





class Zapato(models.Model):
    Id=models.IntegerField(primary_key=True)
    Nombrez=models.CharField(verbose_name="Nombre", max_length=20)
    imgend=models.ImageField(upload_to="projects",verbose_name="imagen", null=True, blank=True)
    precioz=models.PositiveIntegerField(verbose_name="Precio del Producto")
    catego=models.ForeignKey(Categoria,null=True,on_delete=models.SET_NULL)
    gene=models.CharField(choices=gen, null=True, blank=True, max_length=15)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Zapato"
        verbose_name_plural="Zapatos"

    def __str__(self):
        return self.Nombrez
    



