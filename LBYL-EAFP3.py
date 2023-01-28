class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(string):
    if len(string) < 9:
        raise LengthError
    if not any(i.islower() for i in string) or not any(i.isupper() for i in string):
        raise LetterError
    if not any(i.isdigit() for i in string):
        raise DigitError
    return 'Success!'


while True:
    try:
        print(is_good_password(input()))
        break
    except Exception as err:
        print(err.__class__.__name__)
        continue
from sys import stdin

class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(string):
    if len(string) < 9:
        raise LengthError
    if not any(i.islower() for i in string) or not any(i.isupper() for i in string):
        raise LetterError
    if not any(i.isdigit() for i in string):
        raise DigitError
    return 'Success!'


while True:
    try:
        print(is_good_password(input()))
        break
    except Exception as err:
        print(err.__class__.__name__)
        continue
