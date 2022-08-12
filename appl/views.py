from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse 
from django.views.decorators.csrf import csrf_exempt

from appl.models import ProductDetails, UserData
from appl.serializers import ProductSerializer


# Create your views here.

def index(request) :
    return HttpResponse("Hiii Whats up")


def home(request) :
    return render(request, 'welcome.html' )

def login(request) :
    return render(request , 'login.html')


@api_view(['GET'])
def firstApi(request) :
    message = 'Hi How are you '
    return Response(message)


def user_data(request):
    if request.method == 'POST':
        username = request.POST['uname']
        phn = request.POST['phn']
        dob = request.POST['dob']
        email = request.POST['email']
        password = request.POST['passwd']

        userData = UserData(username=username, phone_no=phn, dob=dob, email=email, pswd=password)
        userData.save()

    return render(request , 'form.html')


@csrf_exempt 
def pro_details(request, id = 0):
    if request.method == 'POST' :
        pro_details = JSONParser().parse(request)
        product_serializer = ProductSerializer(data = pro_details)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse({"status" : "success" , "data" : product_serializer.data})
        else :
            return JsonResponse({"status" : "failed" , "data" : product_serializer.errors})

    elif request.method == 'GET' :
        products = ProductDetails.objects.all()  # to get all data in a table
        # products = ProductDetails.objects.get(id = 2) # to get single data in a table dont use many =true!!
        # products = ProductDetails.objects.filter(product_name = 'Laptop')

        product_serializer = ProductSerializer(products, many = True)
        return JsonResponse({"data": product_serializer.data})
    
    elif request.method == 'PUT' :
        products = JSONParser().parse(request)
        productsData = ProductDetails.objects.get(id = products['id'])
        pr_sel = ProductSerializer(productsData, products  )
        if pr_sel.is_valid():
            pr_sel.save()
            return JsonResponse({"status" : "data saved " , "data" : pr_sel.data})
        else :
            return JsonResponse({"status" : "couldnt save data" , "data" : pr_sel.errors})


    elif request.method == 'DELETE' :
        products = JSONParser().parse(request)
        productsData = ProductDetails.objects.filter(id = products['id'])
        productsData.delete()
        
        return JsonResponse({"status" : "data deleted " })
      







