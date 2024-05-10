import json

from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from biryani.models import BiryaniDB
from MyFirstApp.settings import *


# Create your views here.
def get_biryani_details(request):
    try:
        biryani_details = BiryaniDB.objects.all()
    except Exception as e:
        raise Http404("Failed to fetch Biryanis list:- {exc}".format(exc=e))
    # return HttpResponse(["Biryani={0}, Origin_Place={1}\n\n".format(biryani.biryani_name, biryani.origin_place, ) 
    #                         for biryani in biryani_details], content_type="text/plain")
    return render(request, 'biryani/get_all_biryanis_details.html', {'biryanis_details': biryani_details})

def get_biryani_details_by_name(request):
    # try:
    biryani_name = request.GET.get('biryani_name')
    biryani_details = BiryaniDB.objects.filter(biryani_name=biryani_name).values()
    # except BiryaniDB.DoesNotExist:
    #     raise Http404("Biryani '{bn}' doesn't exist".format(bn=biryani_name))
    return render(request, 'biryani/get_biryani_details.html', {'biryani_details': biryani_details[0]})

# @csrf_exempt
def add_biryani_details(request):
    if request.method == 'POST':
        # ## For Python Version < 3.6
        # # biryani_details = request.body.decode('utf-8')
        # # biryani_details = json.loads(biryani_details)

        # ## For Python Version >= 3.6
        # biryani_details = json.loads(request.body)

        # biryani_name = biryani_details.get("biryani_name")
        # return HttpResponse("Added New Biryani Item: {bn}".format(bn=biryani_name))
        biryani_dict = dict()
        biryani_details = request.POST
        biryani_dict['biryani_image'] = request.FILES.get('biryani_image')          # This is the way to get images from frontend
        biryani_dict['biryani_name'] = biryani_details.get('biryani_name')
        biryani_dict['origin_place'] = biryani_details.get('biryani_origin_place')
        biryani_dict['favourite_percentage'] = biryani_details.get('biryani_rating')
        biryani_dict['does_akhila_like'] = True if biryani_details.get('akhila_preference') == 'YES' else False

        # print(biryani_details.get('akhila_preference'))
        # print(biryani_dict['does_akhila_like'])

        BiryaniDB.objects.create(**biryani_dict)
        return redirect('/biryani/add_biryani_details/')        # This will avoid using the already entered values after POST submit and re-initializes all at once.
    return render(request, 'biryani/add_biryani_details.html')

def delete_biryanis(request):
    if request.method == 'POST':
        data = request.POST
        delete_biryani = data.get("biryanis_to_be_deleted")
        BiryaniDB.objects.filter(biryani_name=delete_biryani).delete()
        return redirect('/biryani/delete_biryanis/')
            
    biryanis = BiryaniDB.objects.values_list('biryani_name', flat=True)
    return render(request, 'biryani/delete_biryanis.html', {'biryanis': biryanis})

def delete_biryani_by_name(request, biryani_name):
    biryani = BiryaniDB.objects.filter(biryani_name=biryani_name)
    biryani.delete()
    return redirect('/biryani/')

@csrf_exempt
def update_biryani_details(request):
    if request.method == 'PUT':
        ## For Python Version < 3.6
        # biryani_details = request.body.decode('utf-8')
        # biryani_details = json.loads(biryani_details)

        ## For Python Version >= 3.6
        biryani_details = json.loads(request.body)

        biryani_name = biryani_details.get("biryani_name")
        # print(biryani_name)
        return HttpResponse("Updated Biryani Details: {bn}".format(bn=biryani_name))
