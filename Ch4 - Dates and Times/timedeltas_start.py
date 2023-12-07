#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# TODO: construct a basic timedelta and print it
# print(timedelta(days=365, hours=5, minutes=1))

# # TODO: print today's date
# now = datetime.now()
# print("Today is", now)

# # TODO: print today's date one year from now
# print("One year from now, it will be", str(now + timedelta(days=366)))

# # TODO: create a timedelta that uses more than one argument
# print("In two weeks and three days it will be", str(now + timedelta(weeks=2, days=3)))

# # TODO: calculate the date 1 week ago, formatted as a string
# t = datetime.now() - timedelta(weeks=1)
# s = t.strftime("%A %B %d, %Y")
# print("One week ago it was", s)

### How many days until April Fools' Day?
today = date.today()
april_fools = date(today.year, 4, 1)
if april_fools < today:
    print("April Fools already went by:", ((today-april_fools).days))
    april_fools=april_fools.replace(year = today.year + 1)
# TODO: use date comparison to see if April Fool's has already gone for this year
time_to_april_fools = (april_fools - today).days
print("It is",time_to_april_fools, "days until the next APRIL FOOLS!!!!!!!!!!!!!!!!")
# if it has, use the replace() function to get the date for next year


# TODO: Now calculate the amount of time until April Fool's Day  

