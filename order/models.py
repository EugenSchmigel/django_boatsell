from django.db import models


class Order(models.Model):
    boat = models.ForeignKey('boat.Boat', on_delete=models.CASCADE, verbose_name='Boat')

    name = models.CharField(max_length=150, verbose_name='firstname')
    email = models.EmailField(max_length=150, verbose_name='email')
    message = models.TextField()

    closed = models.BooleanField(default=False, verbose_name='Order closed')

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.boat} from {self.email}'

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'

