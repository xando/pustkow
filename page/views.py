from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from pustkow_osiedle.page.models import *

def fotografie(request):
    return render_to_response('fotografie.html', 
                              {'photos': Photo.objects.all() },
                              context_instance=RequestContext(request))
