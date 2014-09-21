from django.shortcuts import render
from django.http import HttpResponse

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
