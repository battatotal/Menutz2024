from django.db import models
from django.urls import reverse, reverse_lazy


class Menu(models.Model): #Меню
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title


    def __iter__(self):
        return iter(self.Items.all())


    def get_absolute_url(self):
        return reverse('menu', kwargs={'menu_slug': self.slug})


class MenuItems(models.Model): #Элементы меню
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    ancestor = models.ForeignKey('self', related_name="descandances",on_delete=models.CASCADE, null=True, blank=True)
    menu = models.ManyToManyField(to='Menu', related_name='Items', blank=True)

    isroot = models.BooleanField(default=False, verbose_name='Корневой элемент')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('mymenu:menu', kwargs={'item_slug': self.slug})