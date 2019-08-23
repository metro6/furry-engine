from django.db import models
from django.utils.translation import ugettext_lazy as _


class ExtUser(models.Model):
    ext_id = models.PositiveSmallIntegerField(_('Ext user ID'), unique=True, db_index=True)
    name = models.CharField(_('Name'), max_length=64)
    username = models.CharField(_('Username'), max_length=64)
    email = models.EmailField(_('Email'))

    class Meta:
        verbose_name = 'External User'
        verbose_name_plural = 'External Users'

    def __str__(self):
        return self.name


class ExtTariff(models.Model):
    ext_id = models.PositiveSmallIntegerField(_('Ext tariff ID'), unique=True, db_index=True)
    name = models.CharField(_('Name'), max_length=64)
    size = models.CharField(_('Size'), max_length=64)
    websites = models.PositiveSmallIntegerField(_('Websites'))
    databases = models.PositiveSmallIntegerField(_('databases'))

    class Meta:
        verbose_name = 'External Tariff'
        verbose_name_plural = 'External Tariffs'

    def __str__(self):
        return self.name


class ClientInfo(models.Model):
    SUCCESS_STATUSES = (
        (False, 'Not success'),
        (True, 'Success'),
    )
    success = models.CharField(_('Success'), choices=SUCCESS_STATUSES, default=SUCCESS_STATUSES[0][0], max_length=8)
    STATUSES = (
        ('TRIAL', 'Trial'),
        ('MEDIUM', 'Medium'),
        ('NORMAL', 'Large'),
    )
    status = models.CharField(_('Status'), choices=STATUSES, default=STATUSES[0][0], max_length=8)
    client = models.ForeignKey(ExtUser, on_delete=models.CASCADE)
    tariff = models.ForeignKey(ExtTariff, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Client Info'
        verbose_name_plural = 'Clients Info'

    def __str__(self):
        return self.client.name + ' ' + self.tariff.name