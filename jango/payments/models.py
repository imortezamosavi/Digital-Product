from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.validators import validate_phone_number
# Create your models here.

class Gateway(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='Gateway/')
    is_enable = models.BooleanField(_('is enable', default=True))
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'gateways'
        verbose_name = _('Gateway')
        verbose_name_plural = _('Gateways')

class Payment(models.Model):

    STATUS_VOID = 0
    STATUS_PAID = 10
    STATUS_ERROR = 20
    STATUS_CANCELED = 30
    STATUS_REFUNDED = 31
    STATUS_CHOICES = (
        (STATUS_VOID, _('Void')),
        (STATUS_PAID, _('Paid')),
        (STATUS_ERROR, _('Error')),
        (STATUS_CANCELED, _('User Canceled')),
        (STATUS_REFUNDED, _('Refunded')),
    )

    STATUS_TRANSLATIONS = {
        STATUS_VOID, _('Void'),
        STATUS_PAID, _('Paid'),
        STATUS_ERROR, _('Error'),
        STATUS_CANCELED, _('User Canceled'),
        STATUS_REFUNDED, _('Refunded'),
    }

    uesr = models.ForeignKey('users.User', verbose_name = _('user'),related_name= '%(class)s', on_delete = models.CASCADE)
    package = models.ForeignKey('subscriptions.Package', verbose_name = _('package'),related_name= '%(class)s', on_delete = models.CASCADE)
    gateway = models.ForeignKey(Gateway, verbose_name = _('gateway'), related_name= '%(class)s', on_delete = models.CASCADE)
    price = models.PositiveIntegerField(_('Price'), default=0)
    status = models.PositiveSmallIntegerField(_('status'), choices=STATUS_CHOICES, default=STATUS_VOID, db_index=True)
    device_uuid = models.CharField(_(''), max_length=50, blank=True)
    phone_number = models.BigIntegerField(_('phone number'), validator = [validate_phone_number], db_index=True)
    consumed_code = models.PositiveIntegerField(_('consumed reference code'), null=True, db_index=True)
    created_time = models.DateTimeField(_('creation time'), auto_now_add=True, db_index=True)
    updated_time = models.DateTimeField(_('modification time'), auto_now=True)

    class Meta:
        db_table = 'payments'
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')
