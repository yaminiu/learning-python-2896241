#
# Example file for working with Calendars
# LinkedIn Learning Python course by Joe Marini
#


# TODO: import the calendar module
import calendar

# TODO: create a plain text calendar
# c = calendar.TextCalendar(calendar.MONDAY)
# str = c.formatmonth(2023, 12, 8)
# print(str)

# TODO: create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.MONDAY)
str = hc.formatmonth(2024, 12, 8)
print(str)
# TODO: loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month

  
# TODO: The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms


# TODO: Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:

