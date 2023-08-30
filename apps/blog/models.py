from django.db import models

class Blog(models.Model):
    titulos = models.CharField(max_length=150)
    descricao = models.TextField(null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Blog da Amf'
        verbose_name = 'Blogs da amf'
    
    def _str_(self):
        return self.titulo