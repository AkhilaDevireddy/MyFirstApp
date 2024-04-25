from django.shortcuts import render
from django.http import Http404, HttpResponse
from biryani.models import BiryaniDB
from MyFirstApp.settings import *


# Create your views here.
def get_biryani_details(request):
    try:
        biryani_details = BiryaniDB.objects.all()
    except:
        raise Http404("Failed to fetch Biryanis list. Error: {0}".format(biryani_details))
    return HttpResponse(["Biryani={0}, ".format(biryani.biryani_name, biryani.origin_place, ) for biryani in biryani_details])

def get_biryani_details_by_name(request):
    # try:
    biryani_name = request.GET.get('biryani_name')
    biryani_details = BiryaniDB.objects.filter(biryani_name=biryani_name).values()
    # except BiryaniDB.DoesNotExist:
    #     raise Http404("Biryani '{bn}' doesn't exist".format(bn=biryani_name))
    return render(request, 'biryani/get_biryani_details.html', {'biryani_details': biryani_details})
