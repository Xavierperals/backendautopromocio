from django.core.exceptions import ValidationError


def validate_house_price_value(value: int):

    if value < 100_000 or value > 1_000_000:
        raise ValidationError(
            'El valor debe ser superior a 100.000 e inferior a 1.000.000'
        )

