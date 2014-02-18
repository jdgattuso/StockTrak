from twill.commands import *
import time

go('http://stocktrak.com')
fv("1", "3", "USERNAME")
fv("1", "4", "PASSWORD")
submit('5')
follow('Rankings')
submit('4')

fileTimeStamp = (time.strftime("%m%d_%I_%M%p"))
save_html('Path.'+fileTimeStamp+'.xls')
back()
follow('Graph My Portfolio')
save_html('Path.'+fileTimeStamp+'.html')
print 'done'


