from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    price = models.FloatField(verbose_name='Preço')
    score = models.FloatField(verbose_name='Popularidade')
    image = models.ImageField()

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self) -> str:
        return f'{self.name} {self.price} {self.score}'