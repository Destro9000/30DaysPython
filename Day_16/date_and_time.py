'''
Get the current day, month, year, hour, minute and timestamp from datetime module
Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
Today is 5 December, 2019. Change this time string to time.
Calculate the time difference between now and new year.
Calculate the time difference between 1 January 1970 and now.
Think, what can you use the datetime module for? Examples:

    Time series analysis
    To get a timestamp of any activities in an application
    Adding posts on a blog

'''

from datetime import *

now = datetime.now()
now2= {
  'year': now.year,
  'month': now.month,
  'day': now.day,
  'hour': now.hour,
  'minute': now.minute,
  'second': now.second
}
print(now)
print(now2)

now_format = now.strftime("%m/%d/%Y, %H:%M:%S")
print(now_format)

string='5 December, 2019'
date_obj = datetime.strptime(string, '%d %B, %Y')
print(date_obj)

new_year = datetime(year = 2027, month =1, day =1, hour = 0, minute = 0, second = 0)
print(new_year)

difference = new_year - now
print(difference)

old_year = datetime(year = 1970, month =1, day =1, hour = 0, minute = 0, second = 0)
print(now- old_year) 


# it can be user wherever a time or date in needed