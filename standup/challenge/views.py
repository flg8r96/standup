# blah
from django.shortcuts import render
from django.shortcuts import redirect

import traceback
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, loader
import MySQLdb
import sys

#from challenge import models
from challenge.models import User
from challenge.models import MotionHistory
from challenge.models import DeskheightHistory
from challenge.models import Datamart
from challenge.models import DailyWinner

import json
from urlparse import parse_qsl
import datetime
#import main

@csrf_exempt
def index(request):
    encoding = 1    # 0 = urlencode, 1 = json
    if request.method == 'GET':
        template = loader.get_template('index.html')
        print "\nThis is a " + request.method
        #template = loader.get_template('aodl/athome3.html')
        #data = 1
        #c = Context({'data':data})
        sit_status = User.objects.values('name','sit_status')
        mattsit = User.objects.filter(name='Matt').values('sit_status')
        ms = mattsit[0]
        print ms
        mss = ms['sit_status']
        if ms['sit_status']:
            mattsitstr = 'sitting'
        else:
            mattsitstr = 'standing'

        courtneysit = User.objects.filter(name='Courtney').values('sit_status')
        cs = courtneysit[0]
        print cs
        css = cs['sit_status']
        if cs['sit_status']:
            courtneysitstr = 'sitting'
        else:
            courtneysitstr = 'standing'

        string = "Matt is %s and Courtney is %s" % (mattsitstr, courtneysitstr)
        #print(type(sit_status))
        #print(sit_status[0])
        #print(sit_status[1])
        b = sit_status[0]
        #print b['sit_status']
        print "Sit_status: " +str(sit_status)
        #athome = True
        #if b['sit_status']:
        #    sitting = True
        #else:
        #    sitting = False
        #print "Views.py: sitting: " + str(sitting)
        #return HttpResponse(template._render(c))
        #return HttpResponse(string)
        c = Context({'string': string, 'cs': css, 'ms': mss})
        return HttpResponse(template.render(c))

    #sys.exit()
    #return render_to_response('test.html')

    if request.method == 'POST':
        print "This is a " + request.method
        print "body: " + request.body

        # depending on the type encoding used, we decode the packet appropriately
        if encoding:
            parsed = json.loads(request.body)
        else:
            parsed = parse_qsl(request.body)

        # parsing the packet from the sensor
        # each sensor sends the following info:
        # sensor ("stand" or "motion")
        # time (current time in datetime format)
        # data (if sensor = stand then data = distance, else data = T/F for the inmotion state)
        dict_parse = dict(parsed)
        try:
            typeofsensor = dict_parse["typeofsensor"]
            sensorname = dict_parse["sensorname"]
            #deviceid = dict_parse["deviceid"]
            #eventtype = dict_parse["eventtype"]
            dtime = dict_parse["time"]
            data = dict_parse["data"]
            print typeofsensor, sensorname, dtime, data
        except Exception, err:
            print traceback.format_exc()
            print "The json parsing didn't work out."

        # prep the data to be saved in the database
        try:
            # determine the user
            if sensorname == 'Matt':
                user_id = 1                                   # CHANGE THIS TO LOOKUP ASAP
            elif sensorname == "Courtney":
                user_id = 2

            # save the event in the history tables
            if typeofsensor == "stand":
                save = DeskheightHistory(user_id=user_id,
                      height=data)
            elif typeofsensor == "motion":
                save = MotionHistory(user_id=user_id,
                      inmotion_status=data)
            print "Trying to write to db .."
            sr = save.save()
            print "Data persisted ..."
            print "Save result: " +str(sr)

            # save the status of the current user
            if sensorname == "Matt" and typeofsensor == "stand" and data > 15:      # CHANGE THIS TO READ DB
                # Matt is standing
                uid = User.objects.get(id == 1)
                uid.sit_status = True
                uid.save(update_fields=['sit_status'])
                #save = User(name=sensorname, sit_status=True)
            elif sensorname == "Matt" and typeofsensor == "stand" and data < 15:    # CHANGE THIS TO READ DB
                # Matt is sitting
                uid = User.objects.get(id == 1)
                uid.sit_status = False
                uid.save(update_fields=['sit_status'])
                #save = User(name=sensorname, sit_status=False)
            elif sensorname == "Courtney" and typeofsensor == "stand" and data == True:
                # Courtney is standing
                save = User(name=sensorname, sit_status=True)
            elif sensorname == "Courtney" and typeofsensor == "stand" and data == False:
                # Courtney is sitting
                save = User(name=sensorname, sit_status=False)
            print "Trying to write to db .."
            sr = save.save()
            print "Data persisted ..."
            print "Save result: " +str(sr)

        except Exception, err:
            print traceback.format_exc()
            print "The data preparation for saving to the database didn't work out"

        #print "sensorname id: " +str(sensorname) +" Time: " +str(dtime)
        #save = Inmotion(roomid="kitchen", datetime=datetime.datetime.now())
        #save = Inmotion(roomid=sensorname, datetime=dtime)


        # send HTML response to client
        #print "str_parsed .. body_qsl: " + str(parsed)
        #print dict_parse
        response = "Thanks for the info ... douche!" + "\n" + "Here's what you sent: \n" + str(dict_parse)

        return HttpResponse(response)


# Create your views here.
# Create your views here.
