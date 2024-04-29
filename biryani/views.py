import json

from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from biryani.models import BiryaniDB
from MyFirstApp.settings import *


# Create your views here.
def get_biryani_details(request):
    try:
        biryani_details = BiryaniDB.objects.all()
    except:
        raise Http404("Failed to fetch Biryanis list. Error: {0}".format(biryani_details))
    return HttpResponse(["Biryani={0}, Origin_Place={1}\n\n".format(biryani.biryani_name, biryani.origin_place, ) 
                            for biryani in biryani_details], content_type="text/plain")

def get_biryani_details_by_name(request):
    # try:
    biryani_name = request.GET.get('biryani_name')
    biryani_details = BiryaniDB.objects.filter(biryani_name=biryani_name).values()
    # except BiryaniDB.DoesNotExist:
    #     raise Http404("Biryani '{bn}' doesn't exist".format(bn=biryani_name))
    return render(request, 'biryani/get_biryani_details.html', {'biryani_details': biryani_details[0]})

@csrf_exempt
def set_biryani_details(request):
    if request.method == 'POST':
        biryani_details = request.body.decode('utf-8')
        biryani_details = json.loads(biryani_details)
        biryani_name = biryani_details.get("biryani_name")
        return HttpResponse("Added Biryani: {bn}".format(bn=biryani_name))
        
