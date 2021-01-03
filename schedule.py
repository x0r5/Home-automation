import pigpio
import json
import math
import time
from datetime import datetime

pi = pigpio.pi()
print('wakeup run at: ' + str(datetime.now()))
with open('/var/www/html/alarm.json', 'r') as f:
    data = json.load(f)
    red = data['red']
    green = data['green']
    blue = data['blue']

    parts = 10
    wake_up_time = 1 #hours
    wake_up_time = wake_up_time * 60 * 60 #seconds
    wake_up_time = 5
    redlist = []
    bluelist = []
    greenlist = []

    for i in range(parts):
        if(i == 0):
            redlist.append( math.ceil(float(red) / parts) )
            bluelist.append( math.ceil(float(blue) / parts) )
            greenlist.append( math.ceil(float(green) / parts))
        else:
            redlist.append( redlist[i-1] + redlist[0] if (redlist[i-1] + redlist[0]) <= 255 else 255 )
            bluelist.append( bluelist[i-1] + bluelist[0] if (bluelist[i-1] + bluelist[0]) <= 255 else 255 )
            greenlist.append( greenlist[i-1] + greenlist[0] if (greenlist[i-1] + greenlist[0]) <= 255 else 255 )


    for i in range(parts):
        pi.set_PWM_dutycycle(24, redlist[i])
        pi.set_PWM_dutycycle(18, bluelist[i])
        pi.set_PWM_dutycycle(25, greenlist[i])
        time.sleep(float(wake_up_time))
