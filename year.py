import datetime
from random import randint
def is_leap_year(datetime_object):
    datetime_object = datetime.datetime(randint(1, 3000),1,1)
    print(datetime_object)
    if datetime_object.year % 4 == 0:
        return True
    else:
        return False
print(is_leap_year(datetime_object=()))
