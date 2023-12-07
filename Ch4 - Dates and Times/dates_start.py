#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#

from datetime import date
from datetime import time
from datetime import datetime

def main():
    ## DATE OBJECTS
    # TODO: Get today's date from the simple today() method from the date class
    # today = date.today()
    # print("Today is", today)
    # TODO: print out the date's individual components
    # print("Date components:", today.day, today.month, today.year)
    
    # TODO: retrieve today's weekday (0=Monday, 6=Sunday)
    # print("today's weekday # is", today.weekday())
    # days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    # print("Which is a ", days[today.weekday()])
    # DATETIME OBJECTS
    # TODO: Get today's date from the datetime class
    today = datetime.now()
    print("The current date and time is", today)
    
    # TODO: Get the current time
    t = datetime.time(datetime.now())
    print("The current time is", t)
 

  
if __name__ == "__main__":
    main()
  