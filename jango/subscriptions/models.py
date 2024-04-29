from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from utils.validators import validate_sku


class Package(models.Model):
    title = models.CharField(_('title'), max_length=50)
    sku = models.CharField(_('stock keepong unit'), max_length=50, validators=[validate_sku])
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='packages/')
    is_enable = models.BooleanField(_('is enable', default=True))
    price = models.PositiveIntegerField(_('Price'))
    duration = models.DurationField(_('Duration'), blank=True, null=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'packages',
        verbose_name = _('Package')
        verbose_name_plural = _('Package')

    def __str__(self):
        return self.title