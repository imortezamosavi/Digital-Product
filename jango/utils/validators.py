from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

class SKUValidator(RegexValidator):
    regex = '^[a-zA-Z0-9\-\_]{6,20}$'
    message = 'SKU must be alphanumric with 6 to 20 characters'
    code = 'invalid_sku'

class PhoneNumberValidator(RegexValidator):
    regex = r'^\+?1?\d{9,15}$'
    message = 'Phone number must be between 10 and 16 digits'
    code = 'invalid_phone_number'

validate_phone_number = PhoneNumberValidator()
validate_sku = SKUValidator()