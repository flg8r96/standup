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

def index(request):
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

# Create your views here.
# Create your views here.
