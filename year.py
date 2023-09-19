from random import randint
def leap_year():
year = randint(1,3000)
print(year)
if year % 4 == 0:
return True
else:
return False
print(leap_year())
