
from datetime import date

ERROR_MSG = 'expected result for input var {} = {}'
DAYS_IN_YEAR = 365
SPECIAL_DAY_OFFSETS = (100, DAYS_IN_YEAR)
TODAY = date.today()
PROGRAM_START = date(year=2019, month=3, day=23)
AGE_DAYS = (TODAY - PROGRAM_START).days
PROGRAM = 'This bot'

def today_is_special_day(age=None):
    """
    Returns bool if today is a special day (yearly birthday or n of 100 days
    """
    if age is None:
        age = AGE_DAYS
    return any(map(lambda x: age % x == 0, SPECIAL_DAY_OFFSETS))


def days_till_special_day(age=None):
    """
    Calculates days till next special day
    """
    if age is None:
        age = AGE_DAYS
    return min(map(lambda x: x - age % x, SPECIAL_DAY_OFFSETS))


def celebration():
    if today_is_special_day():
        whatday = 'birthday' if AGE_DAYS % DAYS_IN_YEAR == 0 else 'celebration day'
        subject = 'Happy {}!'.format(whatday)
        message = 'This bot was created {} days today, go celebrate!'.format(AGE_DAYS)
    else:
        message = 'No ... days till next birtday: {}, now get back to work!'.format(days_till_special_day())
    return message


