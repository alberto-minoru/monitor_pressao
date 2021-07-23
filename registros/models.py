from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse


class Pressao(models.Model):
    pessoa = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    data = models.DateTimeField('Data')
    sis = models.PositiveIntegerField('Sistólica', validators=[MinValueValidator(1), MaxValueValidator(200)])
    dia = models.PositiveIntegerField('Diastólica', validators=[MinValueValidator(1), MaxValueValidator(120)])
    pul = models.PositiveIntegerField('Pulso', validators=[MinValueValidator(1), MaxValueValidator(150)], blank=True, null=True)
    modificado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Pressão'
        verbose_name_plural = 'Pressões'

    def __str__(self):
        return f"{self.pessoa} - {self.data.strftime('%d/%m/%Y %H:%M')}"

    def get_absolute_url(self):
        return reverse('registro_detail', args=[str(self.id)])
