# day 13 exercise 1

from datetime import datetime

now = datetime.now()                                   
print(now.day, now.month, now.year, now.hour, now.minute, now.timestamp())

print(now.strftime("%m/%d/%Y, %H:%M:%S"))              

t = datetime.strptime("5 December, 2019", "%d %B, %Y") 
print(t)

new_year = datetime(now.year + 1, 1, 1)               
print(new_year - now)

epoch = datetime(1970, 1, 1)                          
print(now - epoch)

# the datetime module can be used for time series analyses, for getting the time stamp of any activity in an application (such as when the user logged in) or for adding date and timr of post on a bllog
