from flask import Flask, request, jsonify
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