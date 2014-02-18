# Scheduling with time Python 2.7        
# using adjusted sleep, single event example
 
import time

hour = int(time.strftime('%H'))
minute = int(time.strftime('%M'))
AMPM = time.strftime('%p')
# 9 pm scheduled event
launchTime = 9

# Calculate hours
if AMPM == 'AM' and hour < launchTime:
        hours = launchTime - hour + 12
elif AMPM == 'AM' and hour > launchTime:
        hours = hour - launchTime + 12
elif AMPM == 'PM' and hour < launchTime:
        hours = launchTime - hour 
else:
        hours = hour - launchTime + 12
# Calculate minutes
if hours == 24:
        minutes = 0
else:
        minutes = 60 - minute

# sleepTime contains the seconds needed to delay until launchTime
sleepTime = hours*3600 + minutes*60

# printed output
print hours ,'hours and', minutes , 'minutes or', sleepTime ,'seconds until 9pm'

