from datetime import datetime, date

from django.core.exceptions import ValidationError


def validate_email(value: str) -> None:
    """
    The validate_email function takes as an argument the verified value of the email field in the form of a string.
    It is designed to check the value of the email field of the User model when creating a new instance.
    Checks whether the value of the field corresponds to the required one. In case of non-compliance, it issues
    a verification error exception from django.core.exceptions module, otherwise returns None.
    """
    if 'rambler.ru' in value :
        raise ValidationError(
            f'{value} registration with rambler.ru prohibited ',
            params={'value': value},
        )


def check_age_new_user(value: datetime.date) -> None:
    """
    The check_age_new_user function takes as an argument the verified value of the birth_date field in the form of
    a datetime.date. It is designed to check the value of the birth_date field of the User model when creating
    a new instance. Checks whether the value of the field corresponds to the required one. In case of non-compliance,
    it issues a verification error exception from django.core.exceptions module, otherwise returns None.
    """
    value_list: list = value.strftime("%y-%m-%d").split('-')
    value_list[0]: str = str(int(value_list[0]) + 9)
    nine_year_date: datetime = datetime.strptime(('-'.join(value_list)), "%y-%m-%d")

    if nine_year_date > datetime.today():
        raise ValidationError('Registration of users under the age of 9 is prohibited.')
