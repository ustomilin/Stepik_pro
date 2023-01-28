from datetime import datetime
def check_coupon(entered_code, correct_code, current_date, expiration_date):
    expiration_date = datetime.strptime(expiration_date, '%B %d %Y')
    current_date = datetime.strptime(current_date, '%B %d %Y')
    if entered_code is not correct_code or current_date < expiration_date:
        return False
    else:
        return True