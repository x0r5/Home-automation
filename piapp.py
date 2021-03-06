from flask import Flask, request, jsonify
from crontab import CronTab
from datetime import date
from datetime import datetime
from datetime import timedelta
import pigpio
import json
import os


app = Flask(__name__)
pi = pigpio.pi()

#API interface for LED controls on the Raspberry, using pigpio daemon

# {{url}}/led?blue=100&red=255&green=10
@app.route('/', methods=['GET'])
def led():

    red = int(request.args.get('red')) if (request.args.get('red')) else 0
    green = int(request.args.get('green')) if (request.args.get('green')) else 0
    blue = int(request.args.get('blue')) if (request.args.get('blue')) else 0

    pi.set_PWM_dutycycle(24, red)
    pi.set_PWM_dutycycle(18, blue)
    pi.set_PWM_dutycycle(25, green)

    with open('/var/www/html/rgb.json', 'w') as f:
        json.dump({"red": red, "green": green, "blue": blue}, f)
    return jsonify({"red": red, "green": green, "blue": blue})


@app.route('/getStatus', methods=['GET'])
def get_status():

    with open('/var/www/html/rgb.json', 'r') as f:
        return json.load(f)

@app.route('/setAlarm', methods=['GET'])
def set_alarm():

    red = int(request.args.get('red')) if (request.args.get('red')) else 0
    green = int(request.args.get('green')) if (request.args.get('green')) else 0
    blue = int(request.args.get('blue')) if (request.args.get('blue')) else 0
    hour = int(request.args.get('hour')) if (request.args.get('hour')) else 0
    minute = int(request.args.get('minute')) if (request.args.get('minute')) else 0

    with open('/var/www/html/alarm.json', 'w') as f:
        json.dump({"red": red, "green": green, "blue": blue, "hour":hour, "minute":minute}, f)

    current_day = date.today()
    if(hour < datetime.now().hour or ( hour == datetime.now().hour and minute < datetime.now().minute )):
        current_day = current_day + timedelta(days=1)
    
    cron = CronTab(user='pi')
    cron.remove_all(comment='led_alarm')
    job = cron.new(command='python3 /var/www/piapp/schedule.py >> /home/pi/alarmlog.txt', comment='led_alarm')
    job.month.on(current_day.month)
    job.day.on(current_day.day)
    job.hour.on(hour - 1)
    job.minute.on(minute)
    job.enable()
    cron.write()

    return jsonify({'Time set for alarm':str(hour-1) + ':' + str(minute)})

@app.route('/stopAlarm', methods=['GET'])
def stop_alarm():
    cron = CronTab(user='pi')
    cron.remove_all(comment='led_alarm')
    cron.write()

    os.system("kill $(pgrep -d',' python3)")
    pi.set_PWM_dutycycle(24, 0)
    pi.set_PWM_dutycycle(18, 0)
    pi.set_PWM_dutycycle(25, 0)
    return jsonify({"answer":"ok"})

@app.route('/getAlarms', methods=['GET'])
def get_alarms():
    cron = CronTab(user='pi')
    ans_json = ''
    all_alarms = cron.find_comment('led_alarm')
    for line in all_alarms:
        if len(ans_json) > 0:
            ans_json += '\n'
        splitted_line = str(line).split()
        ans_json += '' + splitted_line[1] + ':' + splitted_line[0] + ', ' + splitted_line[3] + '.' + splitted_line[2]

    return ans_json