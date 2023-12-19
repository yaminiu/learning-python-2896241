#
# Example file for working with Calendars
# LinkedIn Learning Python course by Joe Marini
#


# TODO: import the calendar module
import calendar

# # TODO: create a plain text calendar
# c = calendar.TextCalendar(calendar.MONDAY)
# # str = c.formatmonth(2023, 12, 8)
# # print(str)

# # TODO: create an HTML formatted calendar
# hc = calendar.HTMLCalendar(calendar.MONDAY)
# str = hc.formatmonth(2024, 12, 8)
# print(str)
# # TODO: loop over the days of a month
# # zeroes mean that the day of the week is in an overlapping month
# for i in c.itermonthdays(2022, 8):
#     print(i)
  
# TODO: The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
# for name in calendar.month_name:
#     print(name)
    
# for day in calendar.day_name:
#     print(day)
    

# TODO: Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:

print("Team meetings will be on:")
for m in range(1, 13):
    cal = calendar.monthcalendar(2024, m)
    # print(cal)
    weekfive = cal[4]
    weekfour = cal[3]
    if weekfive[calendar.MONDAY] != 0:
        meetday = weekfive[calendar.MONDAY]
    else:
        meetday = weekfour[calendar.MONDAY]
    
    print(calendar.month_name[m], meetday)