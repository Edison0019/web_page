from django.db import models

# Create your models here.
class portfolio(models.Model):
    title = models.CharField(max_length=100,verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripcion')
    image = models.ImageField(verbose_name='Imagen',upload_to='portfolio')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de modificacion')

    #this is for stending the configuration of the data model and,
    #showsing meta data and order
    class Meta:
        verbose_name = "projecto"
        verbose_name_plural = "projectos"
        ordering = ["-created"] #the dash signifies the order is desc

    def __str__(self):
        return self.title
    