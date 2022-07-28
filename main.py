from app import create_app
from flask import render_template
import time
import json

app = create_app()

TITLE_INTERZONE = 'signaling internet_unsafe'

list_zone_origin = [
    {
        "name": "Eth-Trunk17.10",
        "flag": True
    }
]
list_zone_destiny = [
    {
        "name": "Eth-Trunk18.252",
        "flag": True
    },
    {
        "name": "Eth-Trunk18.112",
        "flag": False
    }
]

file = open('base.json')
data = json.load(file)


@app.route("/")
def index():
    return render_template('security_output.html',
                           title=TITLE_INTERZONE,
                           time=time.strftime('%A %B, %d %Y %H:%M:%S'),
                           list_zone_origin=list_zone_origin,
                           list_zone_destiny=list_zone_destiny,
                           list_interzone_access=data['data'])
