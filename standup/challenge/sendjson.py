#import RPi.GPIO as GPIO
import time
import urllib2
import json
import datetime

url = "http://localhost:8080/challenge"
url = "http://192.168.1.90:8080/challenge/" # must have the end slash here because APPEND_SLASH is set is django settings
deskheight = 28.1234566
inmotion = True
sendmotion = True

if sendmotion:
    jdata = json.dumps({"typeofsensor": "motion", "sensorname": "Matt", "time": str(datetime.datetime.now()), "data": inmotion})
else:
    jdata = json.dumps({"typeofsensor": "stand", "sensorname": "Matt", "time": str(datetime.datetime.now()), "data": deskheight})

print jdata
print ("Message from localhost -----")
try:
    response = urllib2.urlopen(url, jdata)
    contents = response.read()
    print contents
except urllib2.HTTPError, error:
    contents = error.read()
    print contents
#print response.read()
