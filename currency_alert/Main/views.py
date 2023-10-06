from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from .models import Customer
from .utils import send_mail_
from uagents import Agent, Context
import requests
#from django.auth.models import User
# Create your views here.
currencies=['SGD', 'MYR', 'EUR', 'USD', 'AUD', 'JPY', 'CNH', 'HKD', 'CAD', 'INR', 'DKK', 'GBP', 'RUB', 'NZD', 'MXN', 'IDR', 'TWD', 'THB', 'VND']
def front(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=User.objects.get(email=email)
        if check_password(password, user.password):
            print("user logged in")
            return redirect('currency',user_id=user.id)
    return render(request,"temp.html")

def signup(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        repeat_password=request.POST.get('repeat_password')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        phone_number=request.POST.get('phone')
        user=User.objects.create_user(email=email,password=password,first_name=first_name,last_name=last_name,username=email)
        customer=Customer(email=email,password=password,first_name=first_name,last_name=last_name,phone_number=phone_number)
        customer.save()
        user.save()
        print("user created")
        return redirect('currency',user_id=user.id)
    return render(request,"signup.html")


def currency(request, user_id):
    return render(request, "currency.html", {'user_id': user_id, 'currencies': currencies})

def send_Mail(request):
    send_mail_()
    return render(request,"temp.html")

def convert(request,user_id):
    url = "https://currency-exchange.p.rapidapi.com/listquotes"

    headers = {
	"X-RapidAPI-Key": "2be85388b9msh873d41f7f0cb2c7p127ef4jsn34f1e34ec9c2",
	"X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    print(response.json())
    return render(request,"currency.html",{'user_id':user_id})

