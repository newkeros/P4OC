import datetime


def is_date_valid(date_string):
    format = "%d-%m-%Y"
    try:
        datetime.datetime.strptime(date_string, format)
        return True
    except ValueError:
        return False
