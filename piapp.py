from flask import Flask, request, jsonify
from crontab import CronTab
from datetime import date
import pigpio
import json


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

    red = 255 #int(request.args.get('red')) if (request.args.get('red')) else 0
    green = 255 #int(request.args.get('green')) if (request.args.get('green')) else 0
    blue = 255 #int(request.args.get('blue')) if (request.args.get('blue')) else 0
    hour = int(request.args.get('hour')) if (request.args.get('hour')) else 0
    minute = int(request.args.get('minute')) if (request.args.get('minute')) else 0

    with open('/var/www/html/alarm.json', 'w') as f:
        json.dump({"red": red, "green": green, "blue": blue, "hour":hour, "minute":minute}, f)

    current_day = date.today()
    
    cron = CronTab(user='pi')
    cron.remove_all(comment='led_alarm')
    job = cron.new(command='python3 /var/www/piapp/schedule.py > /home/pi/alarmlog.txt', comment='led_alarm')
    job.month.on(current_day.month)
    job.day.on(current_day.day)
    job.hour.on(hour - 1)
    job.minute.on(minute)
    job.enable()
    cron.write()

    return 'Time set for alarm.'
