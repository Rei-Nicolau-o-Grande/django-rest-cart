from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    price = models.FloatField(verbose_name='Preço')
    score = models.PositiveIntegerField(verbose_name='Popularidade')
    image = models.ImageField()

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['id']

    def __str__(self) -> str:
        return f'{self.name} {self.price} {self.score}'


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Carrinho'
        verbose_name_plural = 'Carrinhos'

    def __str__(self):
        return f'{self.user}'

    @property
    def shipping_cost(self):
        items_total = sum(item.product.price * item.quantity for item in self.items.all())
        if items_total >= 250:
            return 0.00
        else:
            items_count = self.items.count()
            return 10.00 * items_count

    @property
    def subtotal(self):
        items_total = sum(item.product.price * item.quantity for item in self.items.all())
        return items_total

    @property
    def total(self):
        total = self.shipping_cost + self.subtotal
        return total

class ItemCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Produto')
    quantity = models.IntegerField(default=1, verbose_name='Quantidade')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Produto do Carrinho'
        verbose_name_plural = 'Produtos do Carrinho'

    def __str__(self):
        return f'{self.cart} {self.product}'

    @property
    def total_price(self):
        return self.quantity * self.product.price


@receiver(post_save, sender=User)
def create_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)