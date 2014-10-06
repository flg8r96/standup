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

from challenge import models
from challenge.models import user
#from challenge.models import motion_history
#from challenge.models import deskheight_history
#from challenge.models import datamart
#from challenge.models import daily_winner

import json
from urlparse import parse_qsl
import datetime
#import main

def index(request):
    if request.method == 'GET':
        print "\nThis is a " + request.method
        #template = loader.get_template('aodl/athome3.html')
        #data = 1
        #c = Context({'data':data})
    #return HttpResponse(template._render(c))
    return HttpResponse("Hello Worlds")
    #sys.exit()
    #return render_to_response('test.html')

# Create your views here.
# Create your views here.
