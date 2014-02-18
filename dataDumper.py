import time
from twill.commands import *

while 1:
    fileTimeStamp = (time.strftime("%m%d_%I_%M%p"))
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
    sleepTime = int(hours*3600 + minutes*60)

# printed output
    fileTimeStamp = (time.strftime("%m%d_%I_%M%p"))
	print 'Last Runtime:', fileTimeStamp
    print hours ,'hours and', minutes , 'minutes or', sleepTime ,'seconds until 9pm'

    time.sleep(sleepTime)
    
    go('http://stocktrak.com')
    fv("1", "3", "USERNAME")
    fv("1", "4", "PASSWORD")
    submit('5')
    follow('Rankings')
    submit('4')
    save_html('PATH.'+fileTimeStamp+'.xls')
    back()
    follow('Graph My Portfolio')
    save_html('PATH.'+fileTimeStamp+'.html')
