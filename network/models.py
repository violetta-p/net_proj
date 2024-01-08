from django.db import models
from config import settings

NB = {'blank': True, 'null': True}


class Element(models.Model):

    name = models.CharField(max_length=100, unique=True)
    supplier = models.ForeignKey('self', default=None, on_delete=models.SET_DEFAULT, **NB)
    level = models.IntegerField(choices=[(0, 0), (1, 1), (2, 2)])
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Debt to the supplier')
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Network element'
        verbose_name_plural = 'Network elements'
        ordering = ('level', )


class Product(models.Model):

    name = models.CharField(max_length=100, verbose_name='Product name')
    model = models.CharField(max_length=100, verbose_name='Product model')
    release_date = models.DateField(verbose_name='Release date')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Contact(models.Model):

    element = models.OneToOneField(Element, on_delete=models.CASCADE, verbose_name='Network element')
    email = models.EmailField(max_length=200, **NB, verbose_name='Contact email')
    country = models.CharField(max_length=100, **NB, verbose_name='Country')
    city = models.CharField(max_length=100, **NB, verbose_name='City')
    street = models.CharField(max_length=100, **NB, verbose_name='Street')
    building_number = models.CharField(max_length=10, **NB, verbose_name='Building number')

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
