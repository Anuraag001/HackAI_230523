from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from .models import Customer,Alert
from .utils import send_mail_
from uagents import Agent, Context
import time
import requests
import asyncio
from threading import Thread
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

def alert(request):
    return render(request,"alert.html",{"currencies":currencies})


async def do():
    for i in range(10):
        print(i)
        await asyncio.sleep(2)  # Simulate some asynchronous work

async def do2():
    for i in range(10):
        print(i*10)
        await asyncio.sleep(2)

async def main_async(loop):
    f1 = loop.create_task(do()) 
    f2 = loop.create_task(do2()) 
    await asyncio.wait([f1, f2]) 
    loop.close()

alice = Agent(name="alice", seed="alice recovery phrase")
 
@alice.on_interval(period=2.0)
async def say_hello(ctx: Context):
    ctx.logger.info(f'hello, my name is {ctx.name}')

def run_agent():
    alice.run()

# Run the agent in a separate thread
def start_agent():
    run_agent()

# Start the agent in a separate thread when the Django app starts
agent_thread = Thread(target=start_agent)
agent_thread.start()

# Your Django view
def create_alert(request):
    if request.method == 'POST':
        base_currency = request.POST.get('base_currency')
        min_amount = request.POST.get('min_amount')
        max_amount = request.POST.get('max_amount')
        to_currency = request.POST.get('to_currency')
        
        print(min_amount)
        print(max_amount)
        print(base_currency)
        print(to_currency)
        
        alert = Alert(base_currency=base_currency, min_amount=min_amount, max_amount=max_amount, to_currency=to_currency)
        alert.save()
        
        return redirect('screen')

    return render(request, 'create_alert.html')

def screen(request):
    return render(request, 'success.html')


