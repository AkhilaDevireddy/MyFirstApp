from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
# from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate

from biryani.models import BiryaniDB
from MyFirstApp.settings import *


# Create your views here.
def get_biryani_details(request):
    try:
        search_string = request.GET.get('search_biryani_name')
        if search_string:
            biryani_details = BiryaniDB.objects.filter(biryani_name__icontains=search_string)
        else:
            biryani_details = BiryaniDB.objects.all()
    except Exception as e:
        raise Http404("Failed to fetch Biryanis list:- {exc}".format(exc=e))
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
        biryani_dict = dict()
        biryani_details = request.POST
        biryani_dict['biryani_image'] = request.FILES.get('biryani_image')          # This is the way to get images from frontend in django
        biryani_dict['biryani_name'] = biryani_details.get('biryani_name')
        biryani_dict['origin_place'] = biryani_details.get('biryani_origin_place')
        biryani_dict['favourite_percentage'] = biryani_details.get('biryani_rating')
        biryani_dict['does_akhila_like'] = True if biryani_details.get('akhila_preference') == 'YES' else False

        BiryaniDB.objects.create(**biryani_dict)
        return redirect('/biryani/add_biryani_details/')        # This will avoid using the already entered values after POST submit and re-initializes the state all at once.
    return render(request, 'biryani/add_biryani_details.html')

def delete_biryanis(request):
    if request.method == 'POST':
        data = request.POST
        delete_biryani = data.get("biryanis_to_be_deleted")
        BiryaniDB.objects.filter(biryani_name=delete_biryani).delete()
        return redirect('/biryani/delete_biryanis/')            # This will avoid using the already entered values after POST submit and re-initializes the state all at once.
            
    biryanis = BiryaniDB.objects.values_list('biryani_name', flat=True)
    return render(request, 'biryani/delete_biryanis.html', {'biryanis': biryanis})

def delete_biryani_by_name(request, biryani_name):
    biryani = BiryaniDB.objects.filter(biryani_name=biryani_name)
    biryani.delete()
    return redirect('/biryani/')

# @csrf_exempt
def update_biryani_details(request, biryani_name):
    # Details from db
    biryani = BiryaniDB.objects.get(biryani_name=biryani_name)
    if request.method == 'POST':
        # Details from POST
        biryani_dict = dict()
        biryani_details = request.POST
        biryani_dict['biryani_image'] = request.FILES.get('biryani_image')          # This is the way to get images from frontend in django
        biryani_dict['biryani_name'] = biryani_details.get('biryani_name')
        biryani_dict['origin_place'] = biryani_details.get('biryani_origin_place')
        biryani_dict['favourite_percentage'] = biryani_details.get('biryani_rating')
        biryani_dict['does_akhila_like'] = True if biryani_details.get('akhila_preference') == 'YES' else False

        # biryani.update(**biryani_dict)  # Doesn't upload images at the right folder, so following save()

        biryani.biryani_name = biryani_dict['biryani_name']
        biryani.origin_place = biryani_dict['origin_place']
        biryani.favourite_percentage = biryani_dict['favourite_percentage']
        biryani.does_akhila_like = biryani_dict['does_akhila_like']
        biryani.biryani_image = biryani_dict['biryani_image']
        biryani.save()

        return redirect('/biryani/')

    return render(request, 'biryani/update_biryani_details.html', {'biryani_details': biryani})

def login(request):
    if request.method == 'POST':
        user_login_details = request.POST
        username = user_login_details.get('username')
        password = user_login_details.get('password')

        user = User.objects.filter(username=username)
        
        if user.exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')

        user = authenticate(username=username, password=password)

        # if user is None


        if user.exists():
            if password == user[0].password:
                print("HERE-1")
                # return redirect('/')
            else:
                print("HERE-2")
                # return HttpResponse()           # Show error message: Wrong Credentials
        else:
            messages.info(request, "User doesn't exist")
            # print("HERE-3")
            # return HttpResponse()           # Show error message: User Doesn't Exist
        
    return render(request, 'auth/login.html')

def register(request):
    if request.method == 'POST':
        user_login_details = request.POST
        first_name = user_login_details.get('first_name')
        last_name = user_login_details.get('last_name')
        email = user_login_details.get('email')
        username = user_login_details.get('username')
        password = user_login_details.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, 'Username already exists')
            return redirect('/register/')

        user = User.objects.create(
                                    first_name = first_name,
                                    last_name = last_name,
                                    email = email,
                                    username = username
                                )
        user.set_password(password)
        user.save()
        messages.info(request, 'Account created successfully')

        return redirect('/register/')
    return render(request, 'auth/register.html')
