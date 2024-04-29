from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

class SKUValidator(RegexValidator):
    regex = '^[a-zA-Z0-9\-\_]{6,20}$'
    message = 'SKU must be alphanumric with 6 to 20 characters'
    code = 'invalid_sku'

validate_sku = SKUValidator()