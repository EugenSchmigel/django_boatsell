from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Owner(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    email = models.EmailField(verbose_name='Email', unique=True)

    def __str__(self):
        return f'{self.name} {self.email}'

    class Meta:
        verbose_name = 'Owner'
        verbose_name_plural = 'Owners'


class Boat(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    year = models.PositiveSmallIntegerField(**NULLABLE, verbose_name='Baujahr')
    price = models.IntegerField(**NULLABLE, verbose_name='Price')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, verbose_name='Owner')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Boat'
        verbose_name_plural = 'Boats'


class BoatHistory(models.Model):
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE, verbose_name='Boat')
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, verbose_name='Owner', **NULLABLE)

    start_year = models.PositiveSmallIntegerField(**NULLABLE, verbose_name='owned since')
    stop_year = models.PositiveSmallIntegerField(**NULLABLE, verbose_name='owned till')


    def __str__(self):
        return f'{self.boat} {self.start_year} - {self.stop_year}'

    class Meta:
        verbose_name = 'History'
        verbose_name_plural = 'Histories'
