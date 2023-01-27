def is_good_password(string):
    if len(string) >= 9 and any(i.isdigit() for i in string) and any(i.islower() for i in string) and \
            any(i.isupper() for i in string):
        return True
    else:
        return False


print(is_good_password('МойПарольСамыйЛучший111'))
