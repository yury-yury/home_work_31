from django.core.exceptions import ValidationError


def check_status_not_TRUE(value: str) -> None:
    """
    The check_status_not_TRUE function takes as an argument the validated value of the status field as a string.
    It is intended for validating the value of the status field of the Ad model when creating a new instance.
    Checks whether the field value matches the required one. In case of a mismatch, raises a ValidationError
    exception from the django.core.exceptions module, otherwise returns None.
    """
    if value == "TRUE":
        raise ValidationError('The value of the is_published field cannot be TRUE when creating the ad.')
