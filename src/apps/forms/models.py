from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Form(models.Model):
    name = models.CharField(_('Название'), max_length=128)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'

    def __str__(self):
        return self.name